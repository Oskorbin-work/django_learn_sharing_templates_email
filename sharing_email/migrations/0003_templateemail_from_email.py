# Generated by Django 4.1.5 on 2023-01-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing_email', '0002_templateemail_alter_destination_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='templateemail',
            name='from_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
