# Generated by Django 3.2.5 on 2021-08-06 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mega', '0002_discount_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='id_customer',
            new_name='customer',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='id_company',
        ),
        migrations.AddField(
            model_name='operation',
            name='discount',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='mega.discount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operation',
            name='status',
            field=models.CharField(choices=[('Активирован', 'Активирован'), ('Просрочен', 'Просрочен'), ('Заблонирован', 'Заблонирован')], max_length=150),
        ),
    ]
