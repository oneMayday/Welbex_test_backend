# Generated by Django 4.2.1 on 2023-05-24 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_alter_location_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cargo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='deliverycar',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliverycar',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
