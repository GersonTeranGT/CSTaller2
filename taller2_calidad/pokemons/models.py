from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    image = models.URLField(blank=True)
    types = models.ManyToManyField(Type, related_name='pokemons')
    abilities = models.ManyToManyField(Ability, related_name='pokemons')

    def __str__(self):
        return self.name