from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import New, NewCategory
from .serializers import NewSerializer, CategorySerializer


class NewListView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class NewDetailView(RetrieveAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    lookup_field = 'id'


class CategoryListView(ListAPIView):
    queryset = NewCategory.objects.all()
    serializer_class = CategorySerializer
