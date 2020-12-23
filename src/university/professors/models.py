from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    