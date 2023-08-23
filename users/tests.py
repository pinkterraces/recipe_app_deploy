from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
       
        User.objects.create(user='John Doe')

    def test_user_name(self):
        # Get a book object to test
        user = User.objects.get(id=1)
        # Get the metadata for the 'name' field and use it to query its data
        field_label = user._meta.get_field('user').verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, 'user')
    
    def test_user_name_max_length(self):
        # Get a book object to test
        user = User.objects.get(id=1)
        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = user._meta.get_field('user').max_length
        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)