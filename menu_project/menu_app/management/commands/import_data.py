
import csv
from django.core.management.base import BaseCommand
from menu_app.models import Element, MenuMaster

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **kwargs):
        self.import_elements()
        self.import_menus()

    def import_elements(self):
        with open('../element_master.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            elements = [
                Element(
                    element_code=row['element_code'],
                    element_name=row['element_name']
                )
                for row in reader
            ]
            Element.objects.bulk_create(elements, batch_size=100)

    def import_menus(self):
        with open('../menu_master.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            menus = [
                MenuMaster(
                    menu_code=row['menu_code'],
                    menu_name=row['menu_name']
                )
                for row in reader
            ]
            MenuMaster.objects.bulk_create(menus, batch_size=100)
