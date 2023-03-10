# Generated by Django 4.1.3 on 2022-12-03 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_alter_dogs_options_alter_dogs_gender_alter_dogs_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Название породы')),
                ('min_weight', models.IntegerField(verbose_name='Минимальный вес')),
                ('max_weight', models.IntegerField(verbose_name='Максимальный вес')),
                ('min_growth', models.IntegerField(verbose_name='Минимальный рост')),
                ('max_growth', models.IntegerField(verbose_name='Максимальный рост')),
                ('hair_care', models.CharField(max_length=50, verbose_name='Уход за шерстью')),
                ('exercise', models.CharField(max_length=50, verbose_name='Упражнения')),
                ('feeding', models.CharField(max_length=50, verbose_name='Кормление')),
                ('temperament', models.CharField(max_length=50, verbose_name='Темперамент')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Порода',
                'verbose_name_plural': 'Породы',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='dogs',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dogs.breed'),
        ),
    ]
