from django.apps import apps
from django.test import TestCase
from .apps import MainContentConfig

# Create your tests here.
class TestAppMainContent(TestCase):
    def test_app_main_content(self):
        self.assertEqual("main_content", MainContentConfig.name)
        self.assertEqual("main_content", apps.get_app_config("main_content").name)

