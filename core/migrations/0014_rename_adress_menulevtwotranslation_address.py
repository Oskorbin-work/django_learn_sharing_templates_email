# Generated by Django 4.1.5 on 2023-02-12 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_menulevtwotranslation_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menulevtwotranslation',
            old_name='adress',
            new_name='address',
        ),
    ]
