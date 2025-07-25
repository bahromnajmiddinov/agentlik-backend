# Generated by Django 5.0.9 on 2024-10-21 04:53

import management.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_staff_reception_times_alter_staff_phone_number_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='avatar',
            field=models.ImageField(default='management/images/default.png', upload_to=management.models.staff_image_path),
        ),
    ]
