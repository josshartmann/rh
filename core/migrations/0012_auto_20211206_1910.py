# Generated by Django 3.1.1 on 2021-12-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211206_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['joining_date']},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
    ]
