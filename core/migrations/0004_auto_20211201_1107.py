# Generated by Django 3.1.1 on 2021-12-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='legal_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
