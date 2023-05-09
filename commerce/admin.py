from django.contrib import admin
from .models import Product, Cart, Payment, OrderPlaced, Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


admin.site.register(OrderPlaced)
admin.site.register(Category)
