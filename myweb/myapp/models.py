from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email = models.EmailField()

    # Image addition in form
    image = models.FileField(upload_to= 'pic' , null= True)




    def __str__(self):
          return self.name

class Book(models.Model):
    title = models.CharField(max_length=20)
    no_pages = models.IntegerField()
    created_by = models.ForeignKey(Author , on_delete= models.CASCADE, null = True)
    def __str__(self):
          return self.title
