from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural ="Departments"

    def __str__(self):
        return self.name

class Laptopmodel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural ="Laptopmodels"

    def __str__(self):
        return self.name

class Laptop(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    laptopmodel = models.ForeignKey(Laptopmodel, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, unique=True)
    serialno = models.CharField(max_length=100, unique=True)
    barcode = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural ="Laptops"

    def __str__(self):
        return self.user

