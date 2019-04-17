# from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User

class Post(models.Model):
    ID = models.TextField()
    Gender = models.TextField()
    Age = models.IntegerField(default=800)
    Salary = models.FloatField(null = True,blank = True, default = None)
    Loan_amount = models.FloatField(null = True,blank = True, default = None)
    Term = models.IntegerField(default=900)

# Create your models here.
