from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=22)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=22)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
