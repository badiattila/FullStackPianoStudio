from django.test import TestCase
from .forms import PianosPostForm
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your tests here.
class TestPianosPostForm(TestCase):
    def test_can_not_create_a_pianospostform_without_attachment(self):
        form = PianosPostForm({
            'brand' : "Forster",
            'price' : 3000, 
            'age' : 20,
            'description' : "Some description",
            'image' : ''
        })
        self.assertFalse(form.is_valid())

