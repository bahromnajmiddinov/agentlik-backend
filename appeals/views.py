from django.db import models

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AppealSerializer
from .models import Appeal, AppealStatisticPage


class ApealsStatistcsAPIView(APIView):
    queryset = Appeal.objects.all() 
    serializer_class = AppealSerializer
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        # Update page views
        if not AppealStatisticPage.objects.exists():
            AppealStatisticPage.objects.create(views=1)
        else:
            page = AppealStatisticPage.objects.all()[0]
            page.views += 1
            page.save()

        appeal_counts = Appeal.objects.values('status').annotate(count=models.Count('id'))
        data = {
            'Kelib tushgan murojaatlar': Appeal.objects.count(),
            'Jarayonda': sum(item['count'] for item in appeal_counts if item['status'] == 'JR'),
            'Ijro holati': {
                'Ijobiy hal qilinga': sum(item['count'] for item in appeal_counts if item['status'] == 'HQ'),
                'Huquqiy ma\'lumot berilgan': sum(item['count'] for item in appeal_counts if item['status'] == 'MB'),
                'Tushuntirish berilgan': sum(item['count'] for item in appeal_counts if item['status'] == 'TB'),
                'Rad etilgan': sum(item['count'] for item in appeal_counts if item['status'] == 'RE'),
                'Boshqa holatlar bo\'yicha': sum(item['count'] for item in appeal_counts if item['status'] == 'BH'),
            },
            'updated': Appeal.objects.last().updated,
            'views': AppealStatisticPage.objects.all()[0].views,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AppealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    