# Generated by Django 4.2.7 on 2023-12-05 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=100)),
                ('autour', models.CharField(max_length=100)),
                ('gener', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=False)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('membership', models.BooleanField(default=False)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('titile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]
