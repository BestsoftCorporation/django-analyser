from django.shortcuts import render
from .models import Products,Users
from .forms import SearchForm
from django.db.models import Avg,Count,Sum


def home(request):
        return render(request, 'index.html', {'page_title': 'Dashboard'})
def products(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            pro = Products.objects.filter(name__icontains=form.cleaned_data['search']) & Products.objects.filter(price__gt=form.cleaned_data['price'])
            avgPrice = pro.aggregate(Avg('price'))
            countPrice = pro.aggregate(Count('id'))
            sumPrice = pro.aggregate(Sum('price'))
            return render(request, 'products.html', {'page_title': 'Dashboard', 'Products': pro,'SumPrice':sumPrice,'AvgPrice':avgPrice,'CountPrice':countPrice, 'form': form})
    else:
        form = SearchForm()
        pro = Products.objects.all()
        avgPrice=pro.aggregate(Avg('price'))
        countPrice = pro.aggregate(Count('id'))
        sumPrice = pro.aggregate(Sum('price'))
        return render(request, 'products.html', {'page_title': 'Dashboard','Products': pro,'SumPrice':sumPrice,'AvgPrice':avgPrice,'CountPrice':countPrice,'form': form})

def users(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            usr = Users.objects.filter(first_name__icontains=form.cleaned_data['search']) | Users.objects.filter(last_name__icontains=form.cleaned_data['search'])
            return render(request, 'users.html', {'page_title': 'Dashboard','Users': usr,'form': form})
    else:
        form = SearchForm()
        usr = Users.objects.all()
        return render(request, 'users.html', {'page_title': 'Dashboard','Users': usr,'form': form})





