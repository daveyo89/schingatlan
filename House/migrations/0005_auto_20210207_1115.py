# Generated by Django 3.1.2 on 2021-02-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0004_auto_20210131_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='meret',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='telek_meret',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
