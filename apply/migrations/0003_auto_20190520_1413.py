# Generated by Django 2.1.7 on 2019-05-20 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_auto_20190520_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='birth_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of Birth'),
        ),
    ]
