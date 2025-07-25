# Generated by Django 5.0.9 on 2024-10-25 10:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_alter_document_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleDocument',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('link', models.URLField()),
                ('category', models.ManyToManyField(to='documents.documentcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
