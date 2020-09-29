from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.

class Phons(models.Model) : 
    admin_name = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    title_model = models.CharField(max_length= 64)
    price = models.CharField(max_length= 64)
    Processor = models.CharField(max_length= 64)
    RAM =  models.CharField(max_length= 64)
    Storage = models.CharField(max_length= 64)
    Display = models.CharField(max_length= 64)
    Camera = models.CharField(max_length= 64)

    def __str__ (self): 
        return self.title_model