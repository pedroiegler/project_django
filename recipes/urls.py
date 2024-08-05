from django.urls import path
from recipes.views import *

app_name = 'recipes'

urlpatterns = [
    path('', home, name="home"),
    path('recipes/<int:id>/', recipe, name="recipe"),
    path('recipes/categories/<int:category_id>/', category, name="category"),
    path('recipes/search/', lambda request: ..., name="search"),
]
