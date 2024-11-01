from django.contrib import admin

from unfold.admin import ModelAdmin

from .models import Appeal, CommonQuestion


@admin.register(Appeal)
class AppelAdmin(ModelAdmin):
    pass


@admin.register(CommonQuestion)
class CommonQuestionAdmin(ModelAdmin):
    pass
