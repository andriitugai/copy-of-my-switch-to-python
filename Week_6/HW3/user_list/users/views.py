from django.shortcuts import render
from .models import User

def home(request):
    user_list = User.objects.all
    return  render(request, 'home.html', {'users': user_list})


def about(request):
    my_name = 'Andrii Tugai'
    return render(request, 'about.html', {'name': my_name})
