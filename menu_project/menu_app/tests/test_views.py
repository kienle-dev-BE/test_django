
import pytest
from django.urls import reverse
from menu_app.models import MenuMaster, Element, Menu

@pytest.mark.django_db
def test_show_menus_view(client):
    menu_master = MenuMaster.objects.create(menu_code='M001', menu_name='Menu 1')
    element1 = Element.objects.create(element_code='E001', element_name='Element 1')
    element2 = Element.objects.create(element_code='E002', element_name='Element 2')

    menu = Menu.objects.create(menu_code=menu_master)
    menu.elements.add(element1, element2)

    url = reverse('show_menus')
    response = client.get(url)

    assert response.status_code == 200
    assert b'Menu 1' in response.content
    assert b'Element 1' in response.content
    assert b'Element 2' in response.content
