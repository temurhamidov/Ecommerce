from django.urls import path
from .views import home, about, contact, CategoryView, ProductDetail, AddToCart, ShowCart, PlusCart, MinusCart, RemoveCart, Checkout, payment_done

urlpatterns = [
    path('', home),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('payment_done/', payment_done, name='payment_done'),
    path('category/<slug:slug>', CategoryView.as_view(), name='category'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),

    ## Cart
    path('add-to-cart/', AddToCart, name='add-to-cart'),
    path('cart/', ShowCart, name='showcart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('orders/', home, name='orders'),

    path('pluscart/', PlusCart, name='pluscart'),
    path('minuscart/', MinusCart, name='minuscart'),
    path('removecart/<int:id>', RemoveCart.as_view(), name='removecart'),

]