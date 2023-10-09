from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_menu(self):
        menu = Menu.objects.create(title="Japanese Salad", price=5.99, inventory=300)
        self.assertEqual(str(menu), "Japanese Salad : 5.99")