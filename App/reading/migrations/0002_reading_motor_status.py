# Generated by Django 4.2.7 on 2023-11-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='motor_status',
            field=models.BooleanField(default=False),
        ),
    ]