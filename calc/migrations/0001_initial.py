# Generated by Django 3.2.3 on 2021-05-28 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allgroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donarname', models.CharField(max_length=200)),
                ('bloodgroup', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.allgroups')),
            ],
        ),
    ]
