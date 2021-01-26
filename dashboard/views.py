from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', {'page_title': 'Dashboard'})
# Create your views here.
