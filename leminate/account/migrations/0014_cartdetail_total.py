# Generated by Django 2.2.2 on 2019-07-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_cart_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdetail',
            name='total',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
