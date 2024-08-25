from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Product


def price_validator(value):
    if value > 1000:
        raise ValidationError('Product is too expensive')


def description_validator(value):
    if len(value) < 20:
        raise ValidationError('Product must have a good description')


class ProductForm(ModelForm):

    price = forms.DecimalField(max_digits=10, decimal_places=2, validators=[price_validator,])
    description = forms.TextInput(blank=True, validators=[description_validator, ])

    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'stock']
