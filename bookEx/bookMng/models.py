from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    message = models.CharField(max_length= 500, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    def _str_(self):
        return self.message


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/upload')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], default=1)



    def __str__(self):
        return str(self.id)
