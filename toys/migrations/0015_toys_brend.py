# Generated by Django 4.0.5 on 2022-07-11 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0014_alter_coupon_valid_from_alter_coupon_valid_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='toys',
            name='brend',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='toys.brend'),
            preserve_default=False,
        ),
    ]
