# Generated by Django 3.1.1 on 2021-12-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211201_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]