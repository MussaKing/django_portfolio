from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    date_of_death = models.DateTimeField()
    content = models.TextField(blank = True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")