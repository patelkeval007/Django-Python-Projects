# Generated by Django 2.2.2 on 2019-07-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='sales',
            field=models.IntegerField(default=0),
        ),
    ]