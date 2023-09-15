from django.db import models


# Create your models here.




class RaffleEntry(models.Model):
    ticket_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    solicitor = models.CharField(max_length=100)
    
class BingoNumber(models.Model):
    number = models.IntegerField(primary_key=True)
    is_drawn = models.BooleanField(default=False)
    time_drawn = models.TimeField(null=True)
    bingo = models.CharField(max_length=100)
    
class Winner(models.Model):
    ticket_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    solicitor = models.CharField(max_length=100)

