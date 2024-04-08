from django.shortcuts import render
from .models import User, UserData
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(
            username=username, 
        ).exists() or User.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'Sorry user already exists...Try a different username or phone number')
        else:
            if password == confirm_password:
                user = User.objects.create_user(
                    email = email,
                    username=username, phone_number=phone_number, password=password
                )
                user.save()
                if not UserData.objects.filter(
                    user=user
                ).exists():
                    UserData.objects.create(user=user)
                login(request, user)
                return redirect('app:dashbaord')
            else:
                messages.error(request, 'Passwords are not thesame')
    if request.user.is_authenticated:
        return redirect('app:dashbaord')
        
    return render(request , 'signup.html',)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('app:dashbaord')
        else:
            messages.error(request, 'Invalid Credentials!!! try again')
            return redirect('users:signin')
        
    if request.user.is_authenticated:
        return redirect('app:dashbaord')
    
    return render(request, 'login.html')

def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect('users:signin')
    return render(request, 'logout.html')