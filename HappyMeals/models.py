from django.db import models
''' database model '''
class customer(models.Model):
    date = models.DateField()    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=50,default='password')

def __str__(self):
    return self.name
