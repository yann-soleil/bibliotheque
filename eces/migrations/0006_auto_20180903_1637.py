# Generated by Django 2.0.5 on 2018-09-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eces', '0005_auto_20180903_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image',
            field=models.FileField(default='images_defaut/defaultdocument.jpeg', upload_to='Repertoire_Images'),
        ),
        migrations.AlterField(
            model_name='filiere',
            name='image',
            field=models.FileField(default='images_defaut/filieredefaut1.jpg', upload_to='Repertoire_Images'),
        ),
    ]
