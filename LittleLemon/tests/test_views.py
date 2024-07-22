from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from 

class MenuViewTest(TestCase):
    
    def setup(self):
        item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 = Menu.objects.create(title="Waffles", price=80, inventory=100)
        item3 = Menu.objects.create(title="Tiramisu", price=80, inventory=100)

    def test_getall(self):
        item = Menu.objects.all()
        serializer = MenuSerializer