# Generated by Django 5.0.3 on 2024-07-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_quotationmodel_invoicercmodel_hsncode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrymodel',
            name='CallDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]