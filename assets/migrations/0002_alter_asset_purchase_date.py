# Generated by Django 5.0.7 on 2024-07-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
