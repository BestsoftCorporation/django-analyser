from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('',views.home, name='home'),
    path('products',views.products, name='products'),
    path('users',views.users, name='users'),
    path('reviews',views.reviews, name='reviews'),
]