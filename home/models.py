from django.db import models

# Create your models here.
class details(models.Model):
    name= models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    text=models.TextField(max_length=50)


    def __str__(self):
        # Return the username or any desired field
        return self.name
        