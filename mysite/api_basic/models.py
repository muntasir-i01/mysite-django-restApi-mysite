from django.db import models

# Create your models here. Models are the tables of our database

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField()


    def __str__(self) -> str:
        return self.title