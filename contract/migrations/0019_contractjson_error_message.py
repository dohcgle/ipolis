# Generated by Django 4.0.2 on 2022-03-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0018_alter_contractjson_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractjson',
            name='error_message',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
