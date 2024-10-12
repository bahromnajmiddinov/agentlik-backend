from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Document, DocumentCategory


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    # fields = '__all__'
    readonly_fields = ['created', 'updated']


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(ModelAdmin):
    # fields = ['name']
    readonly_fields = ['created', 'updated']
    list_display = ['name']
    search_fields = ['name', 'number', 'issued_date', 'category']
