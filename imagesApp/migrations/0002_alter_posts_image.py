# Generated by Django 4.1.5 on 2023-01-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
