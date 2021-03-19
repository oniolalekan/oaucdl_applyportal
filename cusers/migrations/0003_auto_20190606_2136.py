# Generated by Django 2.2.1 on 2019-06-06 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cusers', '0002_auto_20190606_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses_Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='courses_programme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cusers.Courses_Programme'),
        ),
    ]