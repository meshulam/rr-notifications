# Generated by Django 2.0.5 on 2018-05-20 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180520_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AlterField(
            model_name='account',
            name='opted_in',
            field=models.BooleanField(default=True, verbose_name='Has this account opted in for texts'),
        ),
    ]