# Generated by Django 3.1.2 on 2021-02-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0013_auto_20210207_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='cim',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
