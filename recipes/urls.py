from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('recipes/<int:id>', views.recipes, name='recipe'),
]