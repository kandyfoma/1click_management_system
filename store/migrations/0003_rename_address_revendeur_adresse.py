# Generated by Django 3.2.16 on 2022-11-16 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revendeur',
            old_name='address',
            new_name='adresse',
        ),
    ]
