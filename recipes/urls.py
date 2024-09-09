from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contact/', contact),
]