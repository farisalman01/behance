from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=150)
    cover=models.ImageField(upload_to="media", null= True,blank= True)
    image1= models.ImageField(upload_to="media", null= True,blank= True)
    image2=models.ImageField(upload_to="media", null= True,blank= True)

     
    def __str__(self):
        return self.title