# Generated by Django 5.0.2 on 2024-02-19 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0003_remove_cake_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cake',
            name='berries',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='decorations',
        ),
        migrations.AddField(
            model_name='cake',
            name='berries',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cakes', to='cakes.berry', verbose_name='ягоды'),
        ),
        migrations.AddField(
            model_name='cake',
            name='decorations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cakes', to='cakes.decoration', verbose_name='украшения'),
        ),
    ]