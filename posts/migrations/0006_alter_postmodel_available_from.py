# Generated by Django 5.1.1 on 2024-10-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_postmodel_is_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='available_from',
            field=models.CharField(choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=10),
        ),
    ]
