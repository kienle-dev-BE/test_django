
import pytest
from menu_app.models import Element, MenuMaster, Menu

@pytest.mark.django_db
def test_element_creation():
    element = Element.objects.create(element_code='E001', element_name='Element 1')
    assert element.element_code == 'E001'
    assert element.element_name == 'Element 1'

@pytest.mark.django_db
def test_menu_creation():
    menu_master = MenuMaster.objects.create(menu_code='M001', menu_name='Menu 1')
    element1 = Element.objects.create(element_code='E001', element_name='Element 1')
    element2 = Element.objects.create(element_code='E002', element_name='Element 2')

    menu = Menu.objects.create(menu_code=menu_master)
    menu.elements.add(element1, element2)

    assert menu.menu_code.menu_name == 'Menu 1'
    assert menu.elements.count() == 2
    assert menu.elements.first().element_name == 'Element 1'
