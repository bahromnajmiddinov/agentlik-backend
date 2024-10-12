from django.db import models

from core.models import BaseCategory


class RootCategory(BaseCategory):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubCategory(BaseCategory):
    parent_category = models.ForeignKey(RootCategory, on_delete=models.SET_NULL, related_name='sub_categories', null=True)
    name = models.CharField(max_length=75)

    def __str__(self):
        return f'{self.name} | {self.parent_category}'
