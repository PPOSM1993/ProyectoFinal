# Generated by Django 3.1.7 on 2021-04-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20210412_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefono'),
        ),
    ]
