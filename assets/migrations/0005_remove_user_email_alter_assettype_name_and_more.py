# Generated by Django 5.0.7 on 2024-07-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_alter_asset_asset_type_alter_asset_current_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AlterField(
            model_name='assettype',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='roomnumber',
            name='number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
