from django.db import models

# Create your models here.
class Dorm(models.Model) :
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 10)
    lineId = models.TextField()
    dormName = models.CharField(max_length = 200)
    price = models.TextField()
    location = models.TextField()
    desc = models.TextField()
    