# Generated by Django 4.0.5 on 2022-06-30 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0007_country_coupon_order_type_rename_users_user_worker_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='Worker_Type',
        ),
    ]
