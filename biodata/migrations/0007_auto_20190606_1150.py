# Generated by Django 2.2.1 on 2019-06-06 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0006_auto_20190603_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses_Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='courses_in_programme',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='courses_programme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biodata.Courses_Programme'),
        ),
    ]