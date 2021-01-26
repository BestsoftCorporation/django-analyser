from django.shortcuts import render
from .models import Products,Users
from django.http import HttpResponse

def home(request):
        return render(request, 'index.html', {'page_title': 'Dashboard'})
def products(request):
    pro = Products.objects.all()
    return render(request, 'products.html', {'page_title': 'Dashboard','Products': pro})

def users(request):
    usr = Users.objects.all()
    return render(request, 'users.html', {'page_title': 'Dashboard','Users': usr})



