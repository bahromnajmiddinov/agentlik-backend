from django.db import models


class TimeStamps(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseCategory(TimeStamps):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True
