from django.contrib import admin
from .models import Product, Box, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'width', 'height', 'weight', 'created_at')
    search_fields = ('name',)


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'internal_length', 'internal_width', 'internal_height',
        'max_weight', 'cost', 'created_at'
    )
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product', 'quantity', 'total_weight',
        'recommended_box', 'created_at'
    )
    list_filter = ('product', 'recommended_box')
    search_fields = ('product__name',)
    readonly_fields = ('total_weight',)   # computed automatically in save()