from django.db import models

class Movie(models.Model):
    mdate=models.DateField()
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroin=models.CharField(max_length=30)
    review=models.IntegerField()

    
