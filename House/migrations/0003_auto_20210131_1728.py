# Generated by Django 3.1.2 on 2021-01-31 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0002_auto_20210131_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='data',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='House.data'),
        ),
    ]
