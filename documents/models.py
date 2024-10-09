from django.db import models

from core.models import TimeStamps


class DocumentCategory(TimeStamps):
    name = models.CharField(max_length=150)


class Document(TimeStamps):
    name = models.CharField(max_length=150)
    issued_date = models.DateField()
    number = models.CharField(max_length=20)
    link = models.URLField()
    category = models.ManyToManyField(DocumentCategory)

