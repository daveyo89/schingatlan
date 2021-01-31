# Generated by Django 3.1.2 on 2021-01-31 23:25

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0003_auto_20210131_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='data',
            name='futes',
            field=models.CharField(blank=True, choices=[('gaz', 'gaz'), ('villany', 'villany'), ('kalyha', 'kalyha')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='ingatlan_allapota',
            field=models.CharField(blank=True, choices=[('uj', 'uj'), ('normal', 'normal'), ('felujitando', 'felujitando')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='tajolas',
            field=models.CharField(blank=True, choices=[('E', 'E'), ('D', 'D'), ('K', 'K'), ('NY', 'NY')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='data',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='House.data'),
        ),
    ]
