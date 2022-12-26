from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import DogsForm

def index(request):
    owner = Owner.objects.all()
    return render(request, 'dogs/index.html', {'owner': owner, 'name': 'Имя', 'surmame': 'Фамилия'})

def breed(request):
    dogs = Dogs.objects.all()
    breeds = Breed.objects.all()
    return render(request, 'dogs/breeds.html', {'breeds': breeds, 'dogs': dogs, 'title': 'Породы'})

def dogs(request):
    dogs = Dogs.objects.order_by('breed')
    breeds = Breed.objects.all()
    #dogf=Dogs.objects.filter(breed_id=breed_id)
    return render(request, 'dogs/dogs.html', {'dogs': dogs, 'breeds': breeds, 'title': 'Собаки для разведения'})

def get_breed(request, breed_id):
    dogs = Dogs.objects.filter(breed_id=breed_id)
    breeds = Breed.objects.all()
    breed = Breed.objects.get(pk=breed_id)
    return render(request, 'dogs/onebreed.html', {'dogs': dogs, 'breeds': breeds, 'breed': breed})

def onedog(request, dogs_id):
    #dog_item = Dogs.objects.get(pk=dogs_id)
    dog_item = get_object_or_404(Dogs, pk=dogs_id)
    return render(request, 'dogs/onedog.html', {'dog_item': dog_item})

def add_dog(request):
    if request.method == 'POST':
        form = DogsForm(request.POST)
        if form.is_valid():
            dogs = Dogs.objects.create(**form.cleaned_data)
            return redirect(dogs)
    else:
        form = DogsForm()
    return render(request, 'dogs/add_dog.html', {'form': form})