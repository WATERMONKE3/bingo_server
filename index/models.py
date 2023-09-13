from django.db import models

class BingoCard(models.Model):
    b_column = models.CharField(max_length=100)  # Store B column numbers as a comma-separated string
    i_column = models.CharField(max_length=100)  # Store I column numbers as a comma-separated string
    n_column = models.CharField(max_length=100)  # Store N column numbers as a comma-separated string
    g_column = models.CharField(max_length=100)  # Store G column numbers as a comma-separated string
    o_column = models.CharField(max_length=100)  # Store O column numbers as a comma-separated string
# Create your models here.

class RaffleEntry(models.Model):
    ticket_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    solicitor = models.CharField(max_length=100)
    
class Winner(models.Model):
    ticket_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    solicitor = models.CharField(max_length=100)
