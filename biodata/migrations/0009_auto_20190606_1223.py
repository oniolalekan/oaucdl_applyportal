# Generated by Django 2.2.1 on 2019-06-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0008_personalinfo_application_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='application_number',
            field=models.CharField(default='A00001', editable=False, max_length=10, unique=True),
        ),
    ]
