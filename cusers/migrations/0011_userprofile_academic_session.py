# Generated by Django 2.2.1 on 2020-01-13 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cusers', '0010_customuser_programme_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='academic_session',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='cusers.Programme_Session'),
        ),
    ]