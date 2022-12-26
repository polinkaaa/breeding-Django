from django.db import models

class Dogs(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    gender = models.CharField(max_length=50, verbose_name='Пол')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    breed = models.ForeignKey('Breed', on_delete=models.PROTECT, null=True, verbose_name='Порода')
    owner = models.ForeignKey('Owner', null=True, on_delete=models.PROTECT, verbose_name='Хозяин')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ['owner']


class Breed(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название породы')
    min_weight = models.IntegerField(verbose_name='Минимальный вес')
    max_weight = models.IntegerField(verbose_name='Максимальный вес')
    min_growth = models.IntegerField(verbose_name='Минимальный рост')
    max_growth = models.IntegerField(verbose_name='Максимальный рост')
    hair_care = models.CharField(max_length=50, verbose_name='Уход за шерстью')
    exercise = models.CharField(max_length=50, verbose_name='Упражнения')
    feeding = models.CharField(max_length=50, verbose_name='Кормление')
    temperament = models.CharField(max_length=50, verbose_name='Темперамент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
        ordering = ['title']

    def __str__(self):
        return self.title


class Owner(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house = models.CharField(max_length=50, verbose_name='Дом')
    apartment = models.CharField(max_length=50, blank=True, verbose_name='Квартира')
    passport_series = models.CharField(max_length=4, verbose_name='Серия паспорта')
    passport_number = models.CharField(max_length=6, verbose_name='Номер паспорта')

    class Meta:
        verbose_name = "Хозяин"
        verbose_name_plural = "Хозяева"
        ordering = ['surname']

    def __str__(self):
        return self.city