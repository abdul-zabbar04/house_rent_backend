# Generated by Django 5.1.1 on 2024-09-22 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='slug',
        ),
    ]
