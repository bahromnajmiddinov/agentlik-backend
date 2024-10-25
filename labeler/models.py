from attr.validators import max_len
from django.db import models

from core.models import BaseCategory, TimeStamps
from documents.models import Document
from management.models import Staff
from news.models import New
from polls.models import Poll


class RootCategory(BaseCategory):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubCategory(BaseCategory):
    parent_category = models.ForeignKey(RootCategory, on_delete=models.SET_NULL, related_name='sub_categories', null=True)
    name = models.CharField(max_length=75)

    def __str__(self):
        return f'{self.name} | {self.parent_category}'


class CustomTable(models.Model):
    title = models.CharField(max_length=500)


class CustomTableField(models.Model):
    title = models.CharField(max_length=75)
    text = models.CharField(max_length=75)
    link = models.URLField(null=True, blank=True, help_text='If text is link then add url here')
    table = models.ForeignKey(CustomTable, on_delete=models.CASCADE)


class Page(TimeStamps):
    sub_category = models.OneToOneField(SubCategory, on_delete=models.PROTECT, related_name='pages')
    title = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    tables = models.ManyToManyField(CustomTable, blank=True)
    news = models.ManyToManyField(New, blank=True, through='NewsThroughTable')
    documents = models.ManyToManyField(Document, blank=True, through='DocumentsThroughTable')
    staffs = models.ManyToManyField(Staff, blank=True, through='StaffsThroughTable')
    polls = models.ManyToManyField(Poll, blank=True, through='PollsThroughTable')

    views = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return f'{self.sub_category} | {self.views}'


class CorePageThroughTable(TimeStamps):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class NewsThroughTable(CorePageThroughTable):
    new = models.ForeignKey(New, on_delete=models.CASCADE)


class DocumentsThroughTable(CorePageThroughTable):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    
    
class StaffsThroughTable(CorePageThroughTable):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    staff_category = models.CharField(max_length=300, blank=True, null=True)
    

class PollsThroughTable(CorePageThroughTable):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
