from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    phoneNumber = models.CharField(max_length=32)


class CustomerCompany(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=32)
    state = models.CharField(max_length=2)
    people = models.ForeignKey(People)


class LoanType(models.Model):
    name = models.CharField(max_length=32)


class Lead(models.Model):
    customer = models.ForeignKey(CustomerCompany)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    notes = models.TextField()
    leadFirstName = models.CharField(max_length=64)
    leadLastName = models.CharField(max_length=64)
    leadPhoneNumber = models.CharField(max_length=32)
    leadEmail = models.EmailField()
    loanAmount = models.IntegerField()
    loanRate = models.FloatField()
    loadRateType = models.ForeignKey(LoanType)
    loanCreditScore = models.IntegerField()
    loanMonthlyPayment = models.IntegerField()
    loanTerm = models.IntegerField()
    SCD = models.FloatField()
    oneYearCurr = models.IntegerField()
    currentLender = models.TextField()

