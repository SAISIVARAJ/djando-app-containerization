from django.db import models 
class Users(models.Model):
    First_Name=models.CharField(max_length=27)
    Last_Name=models.CharField(max_length=27)
    Username=models.CharField(max_length=27)
    P1=models.CharField(max_length=17)
    P2=models.CharField(max_length=17)
    Email_Address=models.EmailField()
    Mobile_Number=models.CharField(max_length=15)


