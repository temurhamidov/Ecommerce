from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from .models import User, Customer

from .forms import SignUpForm, CustomerProfileForms

# Create your views here.

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForms()
        return render(request, 'registration/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForms(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Tabriklaymiz, Profile Save Successfully')
        else:
            messages.warning(request, 'Invalid Input Data, Maydonlar Xato ')
        return render(request, 'registration/profile.html', locals())


class Address(View):
    def get(self, request):
        add = Customer.objects.filter(user=request.user)
        return render(request, 'registration/address.html', locals())



