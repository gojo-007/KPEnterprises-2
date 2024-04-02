from django.db import models

# Create your models here.

class GSTModel(models.Model):
    GSTName = models.CharField(max_length=100)
    SGST = models.IntegerField(default=0)
    CGST = models.IntegerField(default=0)


class CostCodeModel(models.Model):
    CostCode = models.IntegerField(default=0)
    Name = models.CharField(max_length=100)
    Remarks = models.TextField() 

class LabourModel(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.TextField() 
    Mobile1 = models.CharField(max_length=100)
    Mobile2 = models.CharField(max_length=100)
    Remarks = models.TextField() 

class ClusterModel(models.Model):
    Name = models.CharField(max_length=100)
    Amount = models.IntegerField(default=0)
    ATM = models.CharField(max_length=100,default='False')
    Branch = models.CharField(max_length=100,default='False')

class PartyModel(models.Model):
    Code = models.IntegerField(default=0)
    PartyName = models.CharField(max_length=100)
    Cluster = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    Address = models.TextField() 
    GSTNo = models.CharField(max_length=100)
    NO1 = models.CharField(max_length=100, null=True, blank=True)
    NO2 = models.CharField(max_length=100, null=True, blank=True)
    NO3 = models.CharField(max_length=100, null=True, blank=True)
    NO4 = models.CharField(max_length=100, null=True, blank=True)
    NO5 = models.CharField(max_length=100, null=True, blank=True)
    NO6 = models.CharField(max_length=100, null=True, blank=True)

class RateModel(models.Model):
    CodeNo = models.CharField(max_length=100)
    Description = models.TextField() 
    HSNCode = models.IntegerField(default=0)
    Unit = models.CharField(max_length=100)
    Rate = models.IntegerField(default=0)
    Remarks = models.TextField() 
    GSTName = models.CharField(max_length=100)
    SGST = models.IntegerField(default=0)
    CGST = models.IntegerField(default=0)
    IGSTName = models.CharField(max_length=100,null=True, blank=True)
    IGST = models.IntegerField(default=0)