
from django.shortcuts import render
from .models import Menu

def show_menus(request):
    menus = Menu.objects.all()[:10]
    return render(request, 'menus.html', {'menus': menus})
