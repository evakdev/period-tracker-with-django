# Generated by Django 3.0.8 on 2021-10-16 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracking', '0009_auto_20211010_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackable',
            name='user',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='trackables', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
