# from django.db import models

# Create your models here.
# class Student(models.Model):
#     stuid= models.IntegerField()
#     stuname= models.CharField(max_length=70)
#     stuemail= models.EmailField(max_length=70)
#     stupass= models.CharField(max_length=70)
#     comment = models.CharField(max_length=50,default='not available')
    

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
