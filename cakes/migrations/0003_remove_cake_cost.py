# Generated by Django 5.0.2 on 2024-02-19 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0002_rename_shape_form_rename_shape_cake_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cake',
            name='cost',
        ),
    ]
