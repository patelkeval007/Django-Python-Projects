# Generated by Django 2.2.2 on 2019-07-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_cartdetail_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
