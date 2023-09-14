from django.db import models


# Create your models here.




class RaffleEntry(models.Model):
    ticket_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    solicitor = models.CharField(max_length=100)
    
class BingoCard(models.Model):
    b_column = models.CharField(max_length=100)  
    i_column = models.CharField(max_length=100) 
    n_column = models.CharField(max_length=100) 
    g_column = models.CharField(max_length=100) 
    o_column = models.CharField(max_length=100) 
class Winner(models.Model):
    ticket_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    solicitor = models.CharField(max_length=100)
