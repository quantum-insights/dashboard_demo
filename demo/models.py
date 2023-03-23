from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Demo(models.Model):
    name= models.CharField(max_length= 200)
    start_date= models.DateField()
    responsible= models.ForeignKey(User, on_delete= models.CASCADE)
    week_number = models.CharField(max_length= 2, blank= True)
    end_date= models.DateField()

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number=='':
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args, **kwargs)


class Invoice(models.Model):
    invoice_no = models.CharField(max_length= 7, unique= True)
    customer_id= models.CharField(max_length= 7, unique= False)
    gender= models.CharField(max_length= 10)
    age= models.IntegerField(max_length=3)
    category = models.CharField(max_length=25)
    quantity = models.IntegerField(max_length=1000)
    price = models.FloatField()
    payment_method= models.CharField(max_length= 25)
    invoice_date= models.DateField()
    shopping_mall= models.CharField(max_length=25)


    def __str__(self):
        return self.invoice_no


