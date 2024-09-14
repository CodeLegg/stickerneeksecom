# Generated by Django 5.1.1 on 2024-09-13 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_remove_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 13, 18, 24, 5, 511488)),
        ),
    ]
