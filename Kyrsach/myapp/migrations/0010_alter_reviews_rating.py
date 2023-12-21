# Generated by Django 5.0 on 2023-12-19 15:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_reviews_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(default='1', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]