from django.contrib import admin

from unfold.admin import ModelAdmin, TabularInline

from .models import Staff, Role, Url


class UrlInlineTable(TabularInline):
    model = Url
    extra = 3


@admin.register(Staff)
class StaffAdmin(ModelAdmin):
    inlines = [UrlInlineTable]
    list_display = ['last_name', 'first_name', 'father_name', 'role', 'phone_number']


@admin.register(Role)
class RoleAdmin(ModelAdmin):
    pass
