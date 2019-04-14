from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Contact)
admin.site.register(models.CustomerCompany)
admin.site.register(models.LoanType)
admin.site.register(models.Lead)
