# Generated by Django 5.0 on 2023-12-19 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_reviews_rating_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='reviews',
            name='A qty value is valid between 1 and 10',
        ),
        migrations.AddConstraint(
            model_name='reviews',
            constraint=models.CheckConstraint(check=models.Q(('rating__gte', 1), ('rating__lt', 6)), name='A qty value is valid between 1 and 10'),
        ),
    ]