# Generated by Django 2.0.5 on 2018-08-06 15:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(default=datetime.datetime(2018, 8, 6, 15, 51, 47, 56259, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
