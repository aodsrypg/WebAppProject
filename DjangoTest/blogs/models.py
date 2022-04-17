from audioop import reverse
from django.db import models

# Create your models here.
class Dorm(models.Model) :
    
    Username = models.CharField(max_length = 200)
    sex = models.CharField(max_length = 200)
    dormName = models.SlugField(max_length = 255,unique=True)
    mateNumber = models.IntegerField()
    rent = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    dormDescription = models.TextField()
    mateHabit = models.TextField()
    comment = models.TextField()
    separateBed = models.CharField(max_length = 200)
    utilityBillType = models.CharField(max_length = 200)
    rentShare = models.CharField(max_length = 200)
    contact = models.CharField(max_length = 200)
    haveRoom = models.CharField(max_length = 200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dormName
 
    def get_url(self):
        return reverse('productDetail',args=[self.dormName])
    
    # name = models.CharField(max_length = 200)
    # phone = models.CharField(max_length = 10)
    # lineId = models.TextField()
    # dormName = models.CharField(max_length = 200)
    # price = models.TextField()
    # location = models.TextField()
    # desc = models.TextField()
    