# Generated by Django 4.2.7 on 2023-12-05 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='titile',
        ),
        migrations.DeleteModel(
            name='book',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
    ]
