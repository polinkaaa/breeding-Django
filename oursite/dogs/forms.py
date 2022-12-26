from django import forms
from .models import Breed

class DogsForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя собаки', widget=forms.TextInput(attrs={"class": "form-control"}))
    gender = forms.CharField(max_length=7, label='Пол собаки', widget=forms.TextInput(attrs={"class": "form-control"}))
    #photo = forms.ImageField(upload_to='photos/%Y/%m/%d/')
    breed = forms.ModelChoiceField(queryset=Breed.objects.all(), label='Порода собаки', widget=forms.Select(attrs={"class": "form-control"}))