from django.db import models

import uuid

from core.models import TimeStamps


class DocumentCategory(TimeStamps):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# class BaseDocument(TimeStamps):
#     pass


class SimpleDocument(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    link = models.URLField()
    category = models.ManyToManyField(DocumentCategory)

    def __str__(self):
        return self.name


class Document(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    link = models.URLField()
    category = models.ManyToManyField(DocumentCategory)
    issued_date = models.DateField(null=True, blank=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    document_number = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f'{self.name} | {self.issued_date}'
