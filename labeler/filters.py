from django_filters import rest_framework as filters
from .models import Page

class PageFilter(filters.FilterSet):
    sub_category = filters.CharFilter(field_name='sub_category__name', lookup_expr='iexact')
    sub_category_slug = filters.CharFilter(field_name='sub_category__slug', lookup_expr='iexact')

    class Meta:
        model = Page
        fields = ['sub_category', 'sub_category_slug']
