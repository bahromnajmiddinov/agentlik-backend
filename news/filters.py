from django.db.models import Q

from django_filters import rest_framework as filters
from .models import New

class NewFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    search = filters.CharFilter(method='filter_by_title_and_text')
    created = filters.DateFilter(field_name='created')
    updated = filters.DateFilter(field_name='updated')

    class Meta:
        model = New
        fields = ['category', 'search', 'created', 'updated']

    def filter_by_title_and_text(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(text__icontains=value)
        )
