from django import forms
from .models import Product

class OrderRecommendationForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        label="Select Product",
        empty_label="-- Choose a product --"
    )
    quantity = forms.IntegerField(
        min_value=1,
        label="Quantity"
    )