# Generated by Django 2.2.8 on 2020-03-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20200306_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipts',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='receipts',
            name='user',
            field=models.IntegerField(),
        ),
    ]
