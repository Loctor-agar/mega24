# Generated by Django 3.2.5 on 2021-08-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активный или нет'),
        ),
    ]
