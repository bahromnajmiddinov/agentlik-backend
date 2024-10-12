from django.contrib import admin

from unfold.admin import ModelAdmin

from .models import Staff, Role


@admin.register(Staff)
class StaffAdmin(ModelAdmin):
    list_display = ['last_name', 'first_name', 'father_name', 'role', 'phone_number']


@admin.register(Role)
class RoleAdmin(ModelAdmin):
    pass
