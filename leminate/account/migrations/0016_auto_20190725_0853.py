# Generated by Django 2.2.2 on 2019-07-25 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20190725_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qoh',
            field=models.IntegerField(default=0),
        ),
    ]
