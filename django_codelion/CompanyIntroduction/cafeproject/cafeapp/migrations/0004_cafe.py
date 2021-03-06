# Generated by Django 4.0.5 on 2022-06-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0003_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('term', models.CharField(max_length=200)),
                ('openState', models.BooleanField()),
                ('myungyul', models.BooleanField()),
            ],
        ),
    ]
