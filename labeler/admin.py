from django.contrib import admin

from unfold.admin import ModelAdmin, TabularInline

from .models import RootCategory, SubCategory, Page, DocumentsThroughTable, NewsThroughTable, StaffsThroughTable, PollsThroughTable


@admin.register(RootCategory)
class RootCategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields =  {'slug': ['name']}


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = ['name', 'parent_category', 'slug']
    prepopulated_fields = {'slug': ['name']}
    list_filter = ['parent_category']


class NewsInline(TabularInline):
    model = NewsThroughTable
    extra = 3
    autocomplete_fields = ['new']


class DocumentsInline(TabularInline):
    model = DocumentsThroughTable
    extra = 3
    autocomplete_fields = ['document']
    

class StaffsInline(TabularInline):
    model = StaffsThroughTable
    extra = 3
    autocomplete_fields = ['staff']


class PollsInline(TabularInline):
    model = PollsThroughTable
    extra = 3
    autocomplete_fields = ['poll']


@admin.register(Page)
class PageAdmin(ModelAdmin):
    inlines = [NewsInline, DocumentsInline, StaffsInline, PollsInline]
    list_filter = ['sub_category', 'sub_category__parent_category']
