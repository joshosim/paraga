from django.shortcuts import render
from users.models import *
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    user_id = request.user.id
    user_data = None
    if User.is_authenticated:
        user_data = get_object_or_404(User, id=user_id)

    return render(request, 'dashboard.html', {'user_data': user_data})


def investment(request):
    return render(request, 'investment.html')


def paystack(request):
    return render(request, 'payStack.html')


def toHome(request):
    return render(request, 'toHome.html')
