from django.shortcuts import render
from .models import Vendor,RepairDelivery,RepairTrans

# Account
from allauth.account.decorators import login_required
from django.contrib.auth.models import User
@login_required
def index(request):
    if request.user.is_authenticated:
        deliveryList=RepairDelivery.objects.all().order_by('id').reverse()
    context={
        'delivery': deliveryList
    }
    return render(request,'repairs/index.html', context)