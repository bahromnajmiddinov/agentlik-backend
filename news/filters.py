from django.db.models import Q

from django_filters import rest_framework as filters
from .models import New

class NewFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    category_slug = filters.CharFilter(field_name='category__slug', lookup_expr='iexact')
    search = filters.CharFilter(method='filter_by_title_and_text')
    created = filters.DateFilter(field_name='created')
    updated = filters.DateFilter(field_name='updated')
    last_news = filters.BooleanFilter(method='filter_last_news')
    limit = filters.NumberFilter(method='filter_limit')

    class Meta:
        model = New
        fields = ['category', 'category_slug', 'search', 'created', 'updated']

    def filter_by_title_and_text(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(text__icontains=value)
        )
    
    def filter_last_news(self, queryset, name, value):
        if value:
            return queryset.filter(active=True).order_by('-created')
        return queryset
    
    def filter_limit(self, queryset, name, value):
        if value:
            return queryset[:value]
        return queryset
        