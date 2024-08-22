
import random
from django.core.management.base import BaseCommand
from menu_app.models import Menu, Element, MenuMaster

class Command(BaseCommand):
    help = 'Create random menus with elements'

    def handle(self, *args, **kwargs):
        menu_codes = list(MenuMaster.objects.all())[:10]
        elements = list(Element.objects.all())

        for menu_code in menu_codes:
            selected_elements = random.sample(elements, 5)
            menu = Menu.objects.create(menu_code=menu_code)
            menu.elements.set(selected_elements)
            menu.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 random menus'))
