# Generated by Django 3.1.3 on 2020-11-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='last',
            field=models.CharField(max_length=30),
        ),
    ]