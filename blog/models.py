from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length= 60000)
    date = models.DateField()



    def __str__(self):
       return self.title