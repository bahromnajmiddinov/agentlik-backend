from django.contrib import admin

from .models import RootCategory, SubCategory

admin.site.register(RootCategory)
admin.site.register(SubCategory)
