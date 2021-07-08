from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from .models import Asset_transaction
from .forms import Asset_transaction_Form


def index(request):
    model = Asset_transaction
    form = Asset_transaction_Form()
    if request.method == 'POST':
        form = Asset_transaction_Form(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.assigned_by = request.user.staff
            fs.save()
            messages.success(request, 'Asset Issued Sucessfully')
            return redirect('/asset_trans')
    
        messages.error(request, 'There was an error, Please Contact Admin, NOT SAVED!!')
    context = {'form': form}
    return render(request, 'asset_transaction/index.html', context)
