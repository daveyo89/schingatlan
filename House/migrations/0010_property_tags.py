# Generated by Django 3.1.2 on 2021-02-07 11:55

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('House', '0009_auto_20210207_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
