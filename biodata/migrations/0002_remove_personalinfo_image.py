# Generated by Django 2.2.1 on 2019-05-23 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='image',
        ),
    ]
