from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Document, DocumentCategory, SimpleDocument


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display = ['number', 'name', 'issued_date']
    readonly_fields = ['created', 'updated']
    search_fields = ['name', 'issued_date', 'number']


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['name']
    search_fields = ['name', 'number', 'issued_date', 'category']


@admin.register(SimpleDocument)
class DocumentSimpleAdmin(ModelAdmin):
    readonly_fields = ['created', 'updated']
