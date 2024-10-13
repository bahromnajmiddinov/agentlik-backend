from django.contrib import admin

from unfold.admin import ModelAdmin

from .models import New, NewCategory


@admin.register(New)
class NewAdmin(ModelAdmin):
    # fields = '__all__'
    readonly_fields = ['created', 'updated']


@admin.register(NewCategory)
class NewCategoryAdmin(ModelAdmin):
    pass
