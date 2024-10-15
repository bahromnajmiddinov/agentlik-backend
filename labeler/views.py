from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import RootCategory, SubCategory, Page
from .serializers import RootCategorySerializer, SubCategorySerializer, PageSerializer


class RootCategoryListView(ListAPIView):
    queryset = RootCategory.objects.all()
    serializer_class = RootCategorySerializer


class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class PageListView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetailView(RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
