# Generated by Django 5.0 on 2023-12-19 15:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_reviews_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together={('name', 'item')},
        ),
    ]
