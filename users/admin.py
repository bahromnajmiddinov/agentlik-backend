from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group

from unfold.admin import ModelAdmin

from .models import CustomUser


admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass