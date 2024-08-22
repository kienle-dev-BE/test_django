
from django.urls import path
from .views import show_menus

urlpatterns = [
    path('', show_menus, name='show_menus'),
]
