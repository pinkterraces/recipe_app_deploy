from django.test import TestCase
from .models import Recipe, User

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
       
       user = User.objects.create(user='John Doe')
       # Set up non-modified objects used by all test methods
       Recipe.objects.create(name='Poached Eggs', cooking_time='10', ingredients='Eggs, Toast', user = user)

    def test_recipe_name(self):
        # Get an object to test
        recipe = Recipe.objects.get(id=1)
        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')
    
    def test_recipe_name_max_length(self):
        # Get an object to test
        recipe = Recipe.objects.get(id=1)
        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = recipe._meta.get_field('name').max_length
        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)

    def test_cooking_time_type(self):
        # Get an object to test
        recipe = Recipe.objects.get(id=1)
        #Get the cooking_time
        cooking_time_value = recipe.cooking_time
        #Check if the value is an integer
        self.assertIsInstance(cooking_time_value, int)

    def test_recipe_ingredients(self):
        # Get an object to test
        recipe = Recipe.objects.get(id=1)
        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('ingredients').verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, 'ingredients')
    
    def test_recipe_ingredients_max_length(self):
        # Get an object to test
        recipe = Recipe.objects.get(id=1)
        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = recipe._meta.get_field('ingredients').max_length
        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 250)

    def test_id_creation(self):
        # Get an object to test
        recipe = Recipe.objects.get(id=1)
        #Check id is not null
        self.assertIsNotNone(recipe.id)  

    def test_get_absolute_url(self):
       book = Recipe.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of book #1
       #and load the URL /books/list/1
       self.assertEqual(Recipe.get_absolute_url(), '/recipes/1')