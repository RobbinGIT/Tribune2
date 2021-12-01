# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2021-11-25 22:57
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='articles/'),
        ),
    ]