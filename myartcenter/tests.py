from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from .models import User

# Create your tests here.

class ApiUrlTest(SimpleTestCase):

    def test_login_url_name(self):
        response = self.client.get(reverse('login'))
        #self.assertEquals(response.status_code,200)

    def test_logout_url_name(self):
        response = self.client.get(reverse('logout'))

    def test_register_url_name(self):
        response = self.client.get(reverse('register'))

    def test_passwordreset_url_name(self):
        response = self.client.get(reverse('change-password'))


# class UserTests(TestCase):

#     @classmethod
#     def setUp(cls):
#         post.objects.Create(title='this is a test')

#     def test_(self):
#         User = User.objects.get(id - 1)
#         expected_post_title = post.title
#         self.assertEquals(expected_post_title, 'this is a test')

