from django.shortcuts import render, redirect
from django.views import View
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import ListView
from django.http import HttpResponse
from django.db.models import Q

from user.models import User, Customer
from .models import Product, Cart, Category, OrderPlaced


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('slug')
        product = Product.objects.filter(category__slug=category)
        context = {
            'products' : product,
        }
        return render(request, 'category.html', context)


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'productdetail.html', locals())


def AddToCart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def ShowCart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40

    return render(request, 'addtocart.html', locals())

class Checkout(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40
        razoramount = int(totalamount * 100)
        return render(request, 'checkout.html', locals())

def payment_done(request):
    return render(request, 'payment_done.html')


def PlusCart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' :totalamount,
        }
        return JsonResponse(data)


def MinusCart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


# def RemoveCart(request, id):
#     if request.method == 'GET':
#         prod_id = id
#         c = Cart.objects.get(Q(product__id=prod_id) & Q(user=request.user))
#         c.delete()
#         user = request.user
#         cart = Cart.objects.filter(user=user)
#         amount = 0
#         for p in cart:
#             value = p.quantity * p.product.discounted_price
#             amount = amount + value
#         totalamount = amount + 40
#         data = {
#             'amount': amount,
#             'totalamount': totalamount,
#         }
#         return JsonResponse(data)

class RemoveCart(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        c = Cart.objects.get(id=id)
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        context = {
            'cart': cart
        }

        return render(request, 'addtocart.html', locals())





