# Generated by Django 4.1.5 on 2023-02-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_basetranslation_menu_one_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menulevonetranslation',
            name='menu_two',
        ),
        migrations.AddField(
            model_name='menulevonetranslation',
            name='menu_two',
            field=models.ManyToManyField(blank=True, null=True, to='core.menulevtwo'),
        ),
    ]
