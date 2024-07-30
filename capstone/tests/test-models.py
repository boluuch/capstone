from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu  # Adjust this import path
from restaurant.serializers import MenuSerializer  # Adjust this import path

class MenuViewTest(TestCase):
    def setUp(self):
        # Initialize the APIClient
        self.client = APIClient()
        # Create test instances of the Menu model
        self.menu1 = Menu.objects.create(name='Pizza', description='Delicious cheese pizza', price=12.99)
        self.menu2 = Menu.objects.create(name='Burger', description='Juicy beef burger', price=9.99)
        self.menu3 = Menu.objects.create(name='Salad', description='Fresh garden salad', price=7.99)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('/api/menu/')  # Adjust URL if needed

        # Serialize the data
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Check if the response is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
