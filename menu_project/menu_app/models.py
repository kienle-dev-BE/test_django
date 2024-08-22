
from django.db import models

class Element(models.Model):
    element_code = models.CharField(max_length=100, unique=True)
    element_name = models.CharField(max_length=255)

    def __str__(self):
        return self.element_name

class MenuMaster(models.Model):
    menu_code = models.CharField(max_length=100, unique=True)
    menu_name = models.CharField(max_length=255)

    def __str__(self):
        return self.menu_name

class Menu(models.Model):
    menu_code = models.ForeignKey(MenuMaster, on_delete=models.CASCADE)
    elements = models.ManyToManyField(Element)

    def __str__(self):
        return self.menu_code.menu_name
