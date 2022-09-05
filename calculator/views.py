from django.shortcuts import render
from django import template

register = template.Library()

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def show_recipe(request, recipe):
    context = {}
    servings = int(request.GET.get('servings', 1))
    for i in DATA:
        if i == recipe:
            context = {
                'recipe': DATA[i]
            }
            for j in context['recipe']:
                context['recipe'][j] *= servings
    return render(request, 'calculator/index.html', context)

