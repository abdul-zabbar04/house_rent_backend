# Generated by Django 5.1.1 on 2024-10-06 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_reviewmodel_user_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ['-on_updated']},
        ),
    ]
