# Generated by Django 3.0.8 on 2021-10-17 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20211017_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
