# Generated by Django 2.2.1 on 2020-01-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cusers', '0008_auto_20200113_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programme_Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
    ]