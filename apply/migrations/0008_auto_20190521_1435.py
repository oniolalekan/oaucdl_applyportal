# Generated by Django 2.2.1 on 2019-05-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0007_auto_20190521_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='courses_in_programme',
            field=models.CharField(choices=[(-1, '--Select Programme--'), ('AP', 'Computer Appreciation'), ('PD', 'Python with Django'), ('MT', 'Computer Maintenance')], default=-1, max_length=2),
        ),
    ]