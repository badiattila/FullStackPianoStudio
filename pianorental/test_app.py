from django.apps import apps
from django.test import TestCase
from .apps import PianorentalConfig

# Create your tests here.
class TestPianorentalConfig(TestCase):
    def test_app(self):
        self.assertEqual("pianorental", PianorentalConfig.name)
        self.assertEqual("pianorental", apps.get_app_config("pianorental").name)

