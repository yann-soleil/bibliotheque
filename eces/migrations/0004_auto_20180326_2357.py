# Generated by Django 2.0.5 on 2018-03-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eces', '0003_auto_20180810_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departement',
            name='image',
            field=models.FileField(default='defaultimage.jpg', upload_to='Repertoire_Images'),
        ),
    ]