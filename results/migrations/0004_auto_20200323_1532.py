# Generated by Django 2.2.8 on 2020-03-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20200320_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentolevels',
            name='grades',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentolevels',
            name='subjects',
            field=models.IntegerField(null=True),
        ),
    ]
