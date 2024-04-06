from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashbaord'),
    path('investment/', investment, name='investment'),
    path('paystack/', paystack, name='paystack'),
    path('toHome/', toHome, name='tohome')
]