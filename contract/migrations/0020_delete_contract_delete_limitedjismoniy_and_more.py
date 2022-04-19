# Generated by Django 4.0.3 on 2022-04-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0019_contractjson_error_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contract',
        ),
        migrations.DeleteModel(
            name='LimitedJismoniy',
        ),
        migrations.DeleteModel(
            name='UnlimitJismoniy',
        ),
        migrations.AlterField(
            model_name='contractjson',
            name='payme_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]