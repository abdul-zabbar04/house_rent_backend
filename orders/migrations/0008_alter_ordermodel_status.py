# Generated by Django 5.1.1 on 2024-10-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_ordermodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10, null=True),
        ),
    ]
