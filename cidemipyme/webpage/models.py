from django.db import models

# Create your models here.

class Company(models.Model):
    legal_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

class CompanyPhones(models.Model):
    company_id = models.ForeignKey(Company)
    phone = models.CharField(max_length=20)

class Members(models.Model):
    company_id = models.ForeignKey(Company)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class MemberPhones(models.Model):
    member_id = models.ForeignKey(Members)
    phone = models.CharField(max_length=20)


