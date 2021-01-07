from django.db import models
from django.utils import timezone
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CareersOpportunity(models.Model):
    opportunity = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    experience = models.CharField(max_length=40)
    isActive = models.BooleanField(default=True)
    skills = models.TextField()
    responsibilities = models.TextField()
    createdOn = models.DateField(default=timezone.now())

    def __str__(self):
        return self.opportunity


class Teams(models.Model):
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=40)
    inAdvisoryBoard = models.BooleanField(default=False)
    in_C_Level = models.BooleanField(default=False)
    createdOn = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name


class Applicant(models.Model):
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = PhoneNumberField(max_length=13)
    resume = models.FileField(upload_to='resumes')
    appliedOn=models.DateField(default=timezone.now())

    def __str__(self):
        return self.name + " " + self.lastName
