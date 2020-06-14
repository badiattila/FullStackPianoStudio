from django.test import TestCase
from .models import Pianos

# Create your tests here

class TestModel(TestCase):
    
    def test_a_piano(self):
        piano = Pianos(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text")
        piano.save()
        self.assertEqual(str(piano), "Forster")