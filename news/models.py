from django.db import models

import uuid

from core.models import TimeStamps, BaseCategory
from users.models import CustomUser


class NewCategory(BaseCategory):

    def __str__(self):
        return self.name


class New(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=150)
    text = models.TextField()
    category = models.ManyToManyField(NewCategory)
    active = models.BooleanField(default=False)

    age_limit = models.PositiveSmallIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
