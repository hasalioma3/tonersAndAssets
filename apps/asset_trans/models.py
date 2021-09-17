from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from apps.assets.models import Asset, Staff

# link assets to Users


class Asset_transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assets = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now=True, null=True)
    assigned_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='Assigned_by')
