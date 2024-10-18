from django.contrib import admin

from unfold.admin import ModelAdmin, TabularInline

from .models import Staff, Role, Url


class UrlInlineTable(TabularInline):
    model = Url
    extra = 3


@admin.register(Staff)
class StaffAdmin(ModelAdmin, admin.ModelAdmin):
    inlines = [UrlInlineTable]
    list_display = ['last_name', 'first_name', 'father_name', 'role', 'phone_number']
    search_fields = ['last_name', 'first_name', 'father_name']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Split the search term into parts
        search_terms = search_term.split()

        # Create a Q object for combining queries
        from django.db.models import Q

        if len(search_terms) >= 3:
            # Filter the queryset based on the combined queries
            queryset = Staff.objects.filter(
                    Q(first_name__icontains=search_terms[1]) |
                    Q(last_name__icontains=search_terms[0]) |
                    Q(father_name__icontains=search_terms[2])
            )
        elif len(search_terms) == 2:
            # Filter the queryset based on the combined queries
            queryset = Staff.objects.filter(
                Q(first_name__icontains=search_terms[1]) |
                Q(last_name__icontains=search_terms[0])
            )
        elif len(search_terms) == 1:
            # Filter the queryset based on the combined queries
            queryset = Staff.objects.filter(last_name__icontains=search_terms[0])
            print(search_terms, search_terms[0])

        return queryset, use_distinct


@admin.register(Role)
class RoleAdmin(ModelAdmin):
    pass
