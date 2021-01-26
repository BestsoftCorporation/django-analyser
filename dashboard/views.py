from django.shortcuts import render
from .models import Products,Users
from .forms import SearchForm


def home(request):
        return render(request, 'index.html', {'page_title': 'Dashboard'})
def products(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            pro = Products.objects.filter(name__icontains=form.cleaned_data['search'])
            return render(request, 'products.html', {'page_title': 'Dashboard', 'Products': pro, 'form': form})
    else:
        form = SearchForm()
        pro = Products.objects.all()
        return render(request, 'products.html', {'page_title': 'Dashboard','Products': pro,'form': form})

def users(request):
    usr = Users.objects.all()
    return render(request, 'users.html', {'page_title': 'Dashboard','Users': usr})



