# Generated by Django 2.2.8 on 2020-03-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipts',
            name='referenceNumber',
        ),
        migrations.RemoveField(
            model_name='receipts',
            name='transactionID',
        ),
        migrations.AddField(
            model_name='receipts',
            name='message',
            field=models.CharField(default='foobar', max_length=100),
        ),
        migrations.AddField(
            model_name='receipts',
            name='paymentReference',
            field=models.CharField(default='foobar', max_length=250),
        ),
        migrations.AddField(
            model_name='receipts',
            name='processorId',
            field=models.CharField(default='foobar', max_length=250),
        ),
        migrations.AddField(
            model_name='receipts',
            name='transactionId',
            field=models.CharField(default='foobar', max_length=100),
        ),
        migrations.AlterField(
            model_name='receipts',
            name='amount',
            field=models.CharField(default='foobar', max_length=250),
        ),
    ]
