from django.shortcuts import render
# Create your views here.
def home(request):
    return render (request, 'recipes/base_templates/base.html', context= {
        'name': 'Matheus'
    })
