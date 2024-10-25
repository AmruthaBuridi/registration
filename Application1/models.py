
from django.db import models
class Student1(models.Model):
    username=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone_number=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    conform_password=models.CharField(max_length=25)

