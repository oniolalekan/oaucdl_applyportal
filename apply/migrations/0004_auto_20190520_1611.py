# Generated by Django 2.1.7 on 2019-05-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0003_auto_20190520_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='apply',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Phone Number'),
        ),
    ]