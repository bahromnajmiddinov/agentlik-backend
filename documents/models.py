from django.db import models

import uuid

from core.models import TimeStamps


class DocumentCategory(TimeStamps):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Document(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    issued_date = models.DateField()
    number = models.CharField(max_length=20)
    link = models.URLField()
    category = models.ManyToManyField(DocumentCategory)

    def __str__(self):
        return f'{self.name} | {self.issued_date} | {self.category}'
