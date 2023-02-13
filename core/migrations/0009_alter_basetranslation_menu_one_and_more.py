# Generated by Django 4.1.5 on 2023-02-09 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_menulevtwotranslation_name_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basetranslation',
            name='menu_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.menulevone'),
        ),
        migrations.AlterField(
            model_name='menulevonetranslation',
            name='menu_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.menulevtwo'),
        ),
    ]