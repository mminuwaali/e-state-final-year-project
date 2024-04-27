from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"


class Purchase(models.Model):
    to_date = models.DateField()
    buyer = models.ForeignKey(User, models.PROTECT)
    from_date = models.DateField(auto_now_add=True)
    apartment = models.ForeignKey("landing.apartment", models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
