from django.db import models
from users.models import User
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text= 'in minutes')
    ingredients = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def calc_difficulty(self):
        print('calc_difficulty')
        ingredients = self.ingredients.split(', ')
        length = len(ingredients)
        #print('length', length)
        if self.cooking_time < 10 and length < 4:
            difficulty = "Easy"
        elif self.cooking_time < 10 and length >= 4:
            difficulty = "Medium"
        elif self.cooking_time >= 10 and length < 4:
            difficulty = "Intermediate"
        elif self.cooking_time >= 10 and length >= 4:
            difficulty = "Hard"
        return difficulty
    
    #difficulty = calc_difficulty(self)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})