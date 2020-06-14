from django.test import TestCase
from django.shortcuts import get_object_or_404, reverse

# Create your tests here.
class TestMainViews(TestCase):

    def test_contact(self):
        response = self.client.get('/main_content/contact/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='contact.html')

    def test_index(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='index.html')

    def test_services(self):
        response = self.client.get('/main_content/services/', follow=True)
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(template_name='services.html')
        
    # def test_gallery(self):
    #     response = self.client.get('/main_content/gallery/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(template_name='galery.html')

    def test_pianos_for_sale(self):
        response = self.client.get('/main_content/pianos_for_sale/', follow=True)
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(template_name='pianos_for_sale.html')
        
    def test_contact_send_success(self):
        response = self.client.post('/main_content/contact_send/',{
                'message': 'Testing your site', 
                'user_email':'attila.badi@gmail.com', 
                'user_fname':'Attila', 
                'user_sname':'Badi'},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='contact_success.html')
        