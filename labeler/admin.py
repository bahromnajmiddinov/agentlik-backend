from django.contrib import admin

from unfold.admin import ModelAdmin, TabularInline

from .models import RootCategory, SubCategory, Page, DocumentsThroughTable, NewsThroughTable, StaffsThroughTable, PollsThroughTable


@admin.register(RootCategory)
class RootCategoryAdmin(ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = ['name', 'parent_category']


class NewsInline(TabularInline):
    model = NewsThroughTable
    extra = 3


class DocumentsInline(TabularInline):
    model = DocumentsThroughTable
    extra = 3
    

class StaffsInline(TabularInline):
    model = StaffsThroughTable
    extra = 3


class PollsInline(TabularInline):
    model = PollsThroughTable
    extra = 3


@admin.register(Page)
class PageAdmin(ModelAdmin):
    inlines = [NewsInline, DocumentsInline, StaffsInline, PollsInline]
