# Generated by Django 4.0.4 on 2022-05-23 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Patient age'),
        ),
    ]