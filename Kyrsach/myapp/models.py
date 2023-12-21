from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.name



class OrderDetail(models.Model):
    customer_username = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField(null=True)
    stripe_payment_intent = models.CharField(max_length=200, null=True)
    has_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reviews(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    item = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    rating = models.IntegerField()
    

    def __str__(self):
        return f"{self.name.username} - {self.item.name}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1) & models.Q(rating__lt=6),
                name="A qty value is valid between 1 and 5",
            )
        ]
        unique_together = ('name', 'item')
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

