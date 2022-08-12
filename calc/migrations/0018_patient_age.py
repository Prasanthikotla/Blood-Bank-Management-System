# Generated by Django 3.2.3 on 2021-10-03 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0017_remove_patient_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]