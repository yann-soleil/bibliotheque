# Generated by Django 2.0.5 on 2018-09-05 11:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eces', '0006_auto_20180903_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departement',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='filiere',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
