# Generated by Django 3.1 on 2022-06-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0003_auto_20220621_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toys',
            name='img',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
