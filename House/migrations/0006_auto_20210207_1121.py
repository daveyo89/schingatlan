# Generated by Django 3.1.2 on 2021-02-07 11:21

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('House', '0005_auto_20210207_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=60, unique=True)),
                ('status', models.CharField(choices=[('H', 'Ház'), ('L', 'Lakás'), ('T', 'Telek')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.AlterField(
            model_name='property',
            name='author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
