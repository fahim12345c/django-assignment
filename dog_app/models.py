from django.db import models

# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=50)
    favoritetoy = models.CharField(max_length=50)

    def __str__(self):
        return self.name
