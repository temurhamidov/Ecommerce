from django.urls import path
from .views import SignUpView, ProfileView, Address

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='sign'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('address/', Address.as_view(), name='address'),

]