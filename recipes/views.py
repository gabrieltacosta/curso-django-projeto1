from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    if request.method == "GET":
        return render(request, 'pages/home.html',
                      context={'recipes': [make_recipe() for _ in range(11)],
        })

def recipes(request, id):
     if request.method == "GET":
        return render(request, 'pages/recipe.html', {'recipe': make_recipe()})
    