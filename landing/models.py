from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name.title()


class Apartment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    owner = models.ForeignKey(User, models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    current = models.ForeignKey(
        User, models.SET_NULL, related_name="+", null=True, blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name.title()


class Image(models.Model):
    image = models.ImageField(upload_to="images")
    apartment = models.ForeignKey(Apartment, models.CASCADE)

    def __str__(self) -> str:
        return f"{self.apartment}'s {self.id} image"
