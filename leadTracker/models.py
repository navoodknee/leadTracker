from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    phoneNumber = models.CharField(max_length=32)

    def __str__(self):
        return self.firstName + " " + self.lastName


class CustomerCompany(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=32)
    state = models.CharField(max_length=2)
    people = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LoanType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Lead(models.Model):
    customer = models.ForeignKey(CustomerCompany, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    leadFirstName = models.CharField(max_length=64)
    leadLastName = models.CharField(max_length=64)
    leadPhoneNumber = models.CharField(max_length=32)
    leadEmail = models.EmailField()
    loanAmount = models.IntegerField()
    loanRate = models.FloatField()
    loadRateType = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    loanCreditScore = models.IntegerField()
    loanMonthlyPayment = models.IntegerField()
    loanTerm = models.IntegerField()
    SCD = models.FloatField()
    oneYearCurr = models.IntegerField()
    currentLender = models.TextField()

    def __str__(self):
        return self.customer.name + " - " + str(self.id)

