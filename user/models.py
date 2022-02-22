
from django.db import models

# Create your models here.
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=32)


    def __str__(self):
        return  (self.username)



class Post(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # attendees=models.ManyToManyField(User,related_name='Post')
    

    def __str__(self):
        return (self.text)    



       
