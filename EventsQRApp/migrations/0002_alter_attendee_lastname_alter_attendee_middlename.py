# Generated by Django 4.2.6 on 2023-10-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsQRApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='LastName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='MiddleName',
            field=models.CharField(max_length=200),
        ),
    ]
