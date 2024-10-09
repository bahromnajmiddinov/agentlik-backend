from django.db import models

from core.models import TimeStamps
from users.models import CustomUser


class NewCategory(TimeStamps):
    name = models.CharField(max_length=150)

class New(TimeStamps):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=150)
    text = models.TextField()
    category = models.ManyToManyField(NewCategory)

    age_limit = models.PositiveSmallIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
