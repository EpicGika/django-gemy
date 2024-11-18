# Generated by Django 5.1.3 on 2024-11-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=list, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='describtion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]
