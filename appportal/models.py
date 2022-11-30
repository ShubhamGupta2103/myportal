from operator import truediv
from django.db import models

from django.utils import timezone

class BloodDonor(models.Model):
    Donerid=models.CharField(primary_key=True,max_length=20)
    Password=models.CharField(max_length=45)
    Name=models.CharField(max_length=30)
    Address=models.TextField()
    Email=models.EmailField(max_length=45)
    Gender=models.CharField(max_length=6)
    Phone=models.CharField(max_length=10)
    Age=models.IntegerField()
    CityName=models.CharField(max_length=45)
    Bloodgroup=models.CharField(max_length=10)

Gender=[
    ("M","Male"),
    ("F","Female")
]

class Experience(models.Model):
    Doner_id=models.CharField(max_length=20)
    Subject=models.CharField(max_length=30)
    Remarks=models.CharField(max_length=200)
    Date=models.DateField(default=timezone.now)

class Health_Campaign(models.Model):
    Campaign_Name=models.CharField(max_length=100)
    Organizer_Name=models.CharField(max_length=45)
    Venue=models.CharField(max_length=50)
    pic=models.FileField(max_length=100,upload_to="appportal/picture",default="")
    Description=models.CharField(max_length=200)
    Date=models.DateField(default=timezone.now)




class Contact(models.Model):
    Name=models.CharField(max_length=45)
    Email=models.EmailField(max_length=45,null=False)
    Phone=models.CharField(max_length=10)
    question=models.TextField()
    Date=models.DateField(default=timezone.now)

class FeedBack(models.Model):
    Name=models.CharField(max_length=45)
    Email=models.EmailField(max_length=45)
    Feedbacktext=models.TextField()
    Rating=models.IntegerField()
    Date=models.DateField(default=timezone.now)

    







