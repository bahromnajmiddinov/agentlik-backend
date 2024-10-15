from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from .models import New, NewCategory
from .serializers import NewSerializer, CategorySerializer
from .filters import NewFilter


class NewsPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100


class NewListView(ListAPIView):
    queryset = New.objects.filter(active=True)
    serializer_class = NewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewFilter
    pagination_class = NewsPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class NewDetailView(RetrieveAPIView):
    '''
    To retrieve about "Agentlik Haqida", send request with id of 36a3e12c-0470-40cd-a07d-18526e5f20f0
    '''
    queryset = New.objects.all()
    serializer_class = NewSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryListView(ListAPIView):
    queryset = NewCategory.objects.all()
    serializer_class = CategorySerializer
