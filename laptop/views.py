from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from django.db.models import Q
from django.views.generic import ListView
from django.core.paginator import Paginator

from allauth.account.decorators import login_required

from .models import Department, Laptop, Laptopmodel
from .forms import DepartmentForm,LaptopmodelForm, LaptopForm
@login_required
def laptops(request):
    url_parameter = request.GET.get("q")
    if url_parameter:
        laptop=Laptop.objects.filter(user__icontains = url_parameter).order_by('id').reverse()
        laptop=Laptop.objects.filter(Q(user__icontains=url_parameter) | Q(barcode__icontains=url_parameter)).order_by('id').reverse()
        paginator = Paginator(laptop,10)
    else:
        laptop=Laptop.objects.all().order_by('id').reverse()
        paginator = Paginator(laptop,10)    
    form = LaptopForm()
    form2= LaptopmodelForm()
    if request.method =="POST":
        form = LaptopForm(request.POST)
        form2 = LaptopmodelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return(HttpResponse('That serial number or barcode has already been assigned'))

        
        if form2.is_valid():
            form2.save()
        return redirect('/laptops')
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'laptop':laptop, 'form':form, 'form2':form2, 'page_obj': page_obj}

    return render(request, 'laptop.html', context)