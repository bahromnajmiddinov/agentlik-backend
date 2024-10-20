from django.contrib import admin

from unfold.admin import ModelAdmin, TabularInline

from .models import New, NewCategory, NewImage


class NewImageInline(TabularInline):
    model = NewImage
    extra = 3


@admin.register(New)
class NewAdmin(ModelAdmin):
    list_filter = ['category']
    readonly_fields = ['created', 'updated', 'views']
    list_display = ['title', 'active', 'age_limit', 'views']
    search_fields = ['title']
    inlines = [NewImageInline]


@admin.register(NewCategory)
class NewCategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
