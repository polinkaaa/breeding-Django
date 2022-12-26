from django.contrib import admin

from .models import Dogs, Breed, Owner

class DogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed', 'name', 'gender', 'owner')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'gender')
    list_filter = ('breed', 'gender')

class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'min_weight', 'max_weight', 'min_growth', 'max_growth', 'hair_care', 'exercise', 'feeding', 'temperament')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'temperament')

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic', 'date_of_birth', 'city', 'street', 'house', 'apartment', 'passport_series', 'passport_number')
    search_fields = ('surname', 'city')

admin.site.register(Dogs, DogsAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Owner, OwnerAdmin)
