# Generated by Django 5.0.4 on 2024-04-27 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='estate',
        ),
    ]