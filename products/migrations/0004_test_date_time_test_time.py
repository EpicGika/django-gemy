# Generated by Django 5.1.3 on 2024-11-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_test_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
