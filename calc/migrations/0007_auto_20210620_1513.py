# Generated by Django 3.2.3 on 2021-06-20 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_auto_20210617_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='bg',
        ),
        migrations.RemoveField(
            model_name='details',
            name='your_choice',
        ),
    ]