from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    height_cm = models.IntegerField()
    hobby = models.CharField(max_length=200)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
