# Generated by Django 3.2.5 on 2021-08-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega', '0005_discount_order_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order_num',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]