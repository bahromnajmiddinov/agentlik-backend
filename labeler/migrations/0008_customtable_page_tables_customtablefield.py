# Generated by Django 5.0.9 on 2024-10-25 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0007_page_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='tables',
            field=models.ManyToManyField(blank=True, to='labeler.customtable'),
        ),
        migrations.CreateModel(
            name='CustomTableField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('text', models.CharField(max_length=75)),
                ('link', models.URLField(blank=True, help_text='If text is link then add url here', null=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeler.customtable')),
            ],
        ),
    ]
