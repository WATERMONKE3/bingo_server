from django.db import models

class BingoCard(models.Model):
    b_column = models.CharField(max_length=100)  # Store B column numbers as a comma-separated string
    i_column = models.CharField(max_length=100)  # Store I column numbers as a comma-separated string
    n_column = models.CharField(max_length=100)  # Store N column numbers as a comma-separated string
    g_column = models.CharField(max_length=100)  # Store G column numbers as a comma-separated string
    o_column = models.CharField(max_length=100)  # Store O column numbers as a comma-separated string
