from rest_framework.generics import ListAPIView

from .models import RootCategory, SubCategory
from .serializers import RootCategorySerializer, SubCategorySerializer


class RootCategoryListView(ListAPIView):
    queryset = RootCategory.objects.all()
    serializer_class = RootCategorySerializer


class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
