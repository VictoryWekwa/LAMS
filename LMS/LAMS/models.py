from django.db import models
from django.utils import timezone

#Create your models here.


class Book(models.Model):
    Title = models.CharField(max_length=250)
    YearOfRelease = models.IntegerField()
    Borrowed = models.BooleanField()
    Returned = models.BooleanField()
    BorrowedDate = models.DateTimeField(default = timezone.now, verbose_name= "Date Borrowed")
    ReturnDate = models.DateTimeField(default = timezone.now, verbose_name = "Date Returned")

    def __str__(self):
        return self.Title
    
