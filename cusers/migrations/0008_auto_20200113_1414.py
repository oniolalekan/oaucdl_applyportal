# Generated by Django 2.2.1 on 2020-01-13 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cusers', '0007_userprofile_programmecourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='programmeCourse',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='programme_Course',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='cusers.Programme_Course'),
            preserve_default=False,
        ),
    ]
