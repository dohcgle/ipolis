# Generated by Django 4.0.1 on 2022-01-05 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clickuz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
