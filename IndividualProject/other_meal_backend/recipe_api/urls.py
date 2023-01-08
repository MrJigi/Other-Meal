from django.urls import path
from . import views

urlpatterns = [
    path('getallrecipes/', views.getAllRecipes),
    path('getbyid/', views.getData),
    path('getRecommended/', views.getBestRated),
    path('getByPrefferance/', views.getByPrefferance)
]