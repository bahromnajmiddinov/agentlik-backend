from django.db import models

from core.models import BaseCategory


class RootCategory(BaseCategory):
    name = models.CharField(max_length=50)


class SubCategory(BaseCategory):
    parent_category = models.ForeignKey(RootCategory, on_delete=models.SET_NULL, related_name='sub_categories', null=True)
