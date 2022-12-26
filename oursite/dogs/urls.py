from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('breed/', breed, name='breed'),
    path('alldogs/', dogs, name='dog'),
    path('breed/<int:breed_id>', get_breed, name='onebreed'),
    path('onedog/<int:dogs_id>', onedog, name='onedog'),
    path('alldogs/add-dog', add_dog, name='add_dog'),
]