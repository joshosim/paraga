from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', log_out, name='logout')
]