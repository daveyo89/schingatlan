# Generated by Django 3.1.2 on 2021-02-07 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0006_auto_20210207_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='types',
            name='description',
        ),
        migrations.RemoveField(
            model_name='types',
            name='name',
        ),
        migrations.AddField(
            model_name='property',
            name='types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='House.types'),
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='House.category'),
        ),
    ]
