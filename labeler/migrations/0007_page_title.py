# Generated by Django 5.0.9 on 2024-10-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0006_alter_rootcategory_slug_alter_subcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
