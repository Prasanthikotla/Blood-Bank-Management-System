# Generated by Django 3.2.3 on 2021-06-11 03:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allgroups',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 6, 11, 3, 14, 26, 732460, tzinfo=utc), verbose_name='date of birth'),
            preserve_default=False,
        ),
    ]
