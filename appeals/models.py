from django.db import models

from core.models import TimeStamps


class Appeal(TimeStamps):
    APPEAL_STATUS_CHOICES = (
        ('JR', 'Jarayonda'),
        ('HQ', 'Ijobiy hal qilingan	'),
        ('MB', 'Huquqiy ma\'lumot berilgan'),
        ('TB', 'Tushuntirish berilgan'),
        ('RE', 'Rad etilgan'),
        ('BH', 'Boshqa holatlar bo\'yicha'),
    )
    
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100, blank=True, null=True)
    work_address = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=150)
    text = models.TextField()
    status = models.CharField(max_length=2, choices=APPEAL_STATUS_CHOICES, default='JR')
    
    def __str__(self):
        return f'{self.full_name} | {self.title}'


class CommonQuestion(TimeStamps):
    title = models.CharField(max_length=250)
    text = models.TextField()
    
    def __str__(self):
        return self.title
