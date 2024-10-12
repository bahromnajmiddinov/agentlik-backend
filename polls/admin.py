from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from .models import Poll, Choice


class ChoiceInline(TabularInline):
    model = Choice
    extra = 3
    fields = ['answer']


@admin.register(Poll)
class PollAdmin(ModelAdmin):
    inlines = [ChoiceInline]
    search_fields = ['question']
