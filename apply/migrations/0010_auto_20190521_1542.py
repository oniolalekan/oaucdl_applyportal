# Generated by Django 2.2.1 on 2019-05-21 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0009_auto_20190521_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]