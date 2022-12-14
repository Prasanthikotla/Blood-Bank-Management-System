# Generated by Django 3.2.3 on 2021-07-27 06:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0014_patient_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allgroups',
            name='dob',
        ),
        migrations.AddField(
            model_name='allgroups',
            name='age',
            field=models.IntegerField(default=datetime.datetime(2021, 7, 27, 6, 23, 16, 390909, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='allgroups',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobileNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='PhoneNumber',
            field=models.IntegerField(),
        ),
    ]
