from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
class Status(models.Model):
   Namestatus = models.CharField(max_length=255)


class Personnel_information(models.Model):
    fristname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Phone_number = models.IntegerField(max_length=10)
    Email = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    Criterion = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Degree_Certificate = models.CharField(max_length=255)
    test_date = models.DateField(max_length=255)
    Startdate = models.DateField(max_length=255)
    Date_you_can_request_position = models.DateField(max_length=255)

class request_position(models.Model):
    Assessment_date = models.DateField(max_length=255)
    NameResearchwork = models.CharField(max_length=255)
    Research_base = models.CharField(max_length=255)
    Date = models.DateField(max_length=255)
    Research_level = models.IntegerField(max_length=255)
    Theresult_of_theoperation = models.CharField(max_length=255)
    Criterion = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)

class Criterion(models.Model):
    NameResearch = models.CharField(max_length=255)
    NameResearchbase = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
    Research_level = models.IntegerField(max_length=10)
    book = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.NameResearch)