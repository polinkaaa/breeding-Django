# Generated by Django 4.1.3 on 2022-12-07 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0004_alter_dogs_breed_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='dog',
        ),
        migrations.AddField(
            model_name='dogs',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dogs.owner', verbose_name='Хозяин'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='apartment',
            field=models.CharField(blank=True, max_length=50, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='house',
            field=models.CharField(max_length=50, verbose_name='Дом'),
        ),
    ]