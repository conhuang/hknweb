# Generated by Django 2.2.8 on 2020-03-25 05:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0018_auto_20200317_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deptour',
            name='phone',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number.', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
