# Generated by Django 3.2.3 on 2021-07-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_auto_20210703_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=200)),
                ('dmobile', models.CharField(max_length=10)),
                ('dmail', models.CharField(max_length=50)),
                ('dtext', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'calc_services',
            },
        ),
        migrations.RemoveField(
            model_name='allgroups',
            name='password',
        ),
        migrations.RemoveField(
            model_name='allgroups',
            name='username',
        ),
    ]
