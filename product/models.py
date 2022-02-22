from django.db import models

from django.contrib.auth.models import User

# Create your models here

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    price=models.IntegerField()
    created_at = models.DateField()
    updated_at= models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return  (self.Product)