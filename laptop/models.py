from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from assets.models import Asset
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class Laptop_trans(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    laptop = models.OneToOneField(
        Asset, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Laptops"

    def __str__(self):
        return self.user
