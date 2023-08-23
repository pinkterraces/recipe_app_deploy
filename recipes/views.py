from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_chart

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):                           #class-based view
   model = Recipe                                         #specify model
   template_name = 'recipes/recipes.html'                 #specify template

class RecipeDetailView(LoginRequiredMixin, DetailView):                       #class-based view
   model = Recipe                                        #specify model
   template_name = 'recipes/detail.html' 

def search(request):
   #create an instance of SalesSearchForm that you defined in sales/forms.py
  form = RecipesSearchForm(request.POST or None)
  recipes_df = None
  chart = None

  #check if the button is clicked
  if request.method =='POST':
      #read book_title and chart_type
      recipe_title = request.POST.get('recipe_title')
      chart_type = request.POST.get('chart_type')
      #display in terminal - needed for debugging during development only
      print (recipe_title, chart_type)

      #apply filter to extract data
      qs = Recipe.objects.filter(name=recipe_title)
      if qs:      #if data found
          #convert the queryset values to pandas dataframe
          recipes_df = pd.DataFrame(qs.values())
          #call get_chart by passing chart_type from user input, sales dataframe and labels
          chart = get_chart(chart_type, recipes_df, labels=recipes_df['name'].values)
          recipes_df = recipes_df.to_html()

      print('********************')
      print ('Exploring querysets:')
      print ('Case 1: Output of Recipe.objects.all()')
      qs = Recipe.objects.all()
      print (qs)
      print('********************')
      print ('Case 2: Output of Recipe.objects.filter(recipe_name=recipe_title)')
      qs = Recipe.objects.filter(name=recipe_title)
      print (qs)
      print('********************')
      print ('Case 3: Output of qs.values')
      print (qs.values())
      print('********************')
      print ('Case 4: Output of qs.values_list()')
      print (qs.values_list())
      print('********************')
      print ('Case 5: Output of Recipe.objects.get(id=2)')
      obj = Recipe.objects.get(id=2)
      print (obj)
      print('********************')
      print('********************')
  #pack up data to be sent to template in the context dictionary
  context={
           'form': form,
           'recipes_df': recipes_df,
           'chart': chart
  }
  #load the sales/record.html page using the data that you just prepared  
  return render(request, 'recipes/search.html', context)
