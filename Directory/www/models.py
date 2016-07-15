from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    team = models.CharField(max_length=20)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
