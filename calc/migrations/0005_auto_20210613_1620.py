# Generated by Django 3.2.3 on 2021-06-13 10:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_auto_20210613_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='allgroups',
            name='mail_id',
            field=models.CharField(default=datetime.datetime(2021, 6, 13, 10, 49, 54, 181402, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allgroups',
            name='mobile',
            field=models.CharField(default=datetime.datetime(2021, 6, 13, 10, 50, 8, 981239, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allgroups',
            name='place',
            field=models.CharField(default=datetime.datetime(2021, 6, 13, 10, 50, 21, 346674, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]