# Generated by Django 4.0.2 on 2022-03-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0017_rename_transaction_order_id_contractjson_transaction_order_key'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractjson',
            options={'verbose_name': 'Полис', 'verbose_name_plural': 'Полиса'},
        ),
        migrations.AddField(
            model_name='contractjson',
            name='applicant_fond',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
