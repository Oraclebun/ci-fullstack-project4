# Generated by Django 2.2.14 on 2020-08-20 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mykitchen', '0009_auto_20200820_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='threshold',
            field=models.IntegerField(help_text='Number of days before expiry date to notify me'),
        ),
    ]
