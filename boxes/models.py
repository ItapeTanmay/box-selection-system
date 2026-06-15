from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField(help_text="Length in cm")
    width = models.FloatField(help_text="Width in cm")
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Box(models.Model):
    name = models.CharField(max_length=100)
    internal_length = models.FloatField(help_text="Inner length in cm")
    internal_width = models.FloatField(help_text="Inner width in cm")
    internal_height = models.FloatField(help_text="Inner height in cm")
    max_weight = models.FloatField(help_text="Maximum weight capacity in kg")
    cost = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="Shipping cost in ₹"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (₹{self.cost})"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_weight = models.FloatField(
        help_text="Total order weight (product.weight * quantity)"
    )
    recommended_box = models.ForeignKey(
        Box, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.product.name} x{self.quantity}"

    def save(self, *args, **kwargs):
        # Auto-calculate total weight before saving
        if not self.total_weight:
            self.total_weight = self.product.weight * self.quantity
        super().save(*args, **kwargs)