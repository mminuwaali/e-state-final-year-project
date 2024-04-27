from . import models
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = ["name"]
        model = models.Category


class apartmentForm(forms.ModelForm):
    class Meta:
        model = models.Apartment
        fields = ["name", "category", "price", "owner"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ["image", "apartment"]
