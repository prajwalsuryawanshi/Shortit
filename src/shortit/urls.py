from django.urls import path 
from .views import home , createshorturl , redirect

urlpatterns = [
    path(''  , home),
    path('create/', createshorturl , name = 'create'),
    path('<str:url>' , redirect , name = 'redirect')
]