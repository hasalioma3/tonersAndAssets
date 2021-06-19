from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView
from django.core.paginator import Paginator

from allauth.account.decorators import login_required

from .models import Toners
from .forms import TonerForm,BranchForm

from django import template
@login_required
def Index(request):
    url_parameter = request.GET.get("q")
    if url_parameter:
        toners=Toners.objects.filter(branch__name__icontains = url_parameter).order_by('id').reverse()
        paginator = Paginator(toners,10)
    else:
        toners= Toners.objects.all().order_by('id').reverse()
        paginator = Paginator(toners,10)    
    form = TonerForm()
    form2= BranchForm()
    if request.method =="POST":
        form = TonerForm(request.POST)
        form2 = BranchForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.created_by = request.user
            fs.save()
        if form2.is_valid():
            fs= form2.save()
        return redirect('/')
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'toners':toners, 'form':form, 'form2':form2, 'page_obj': page_obj}

    register = template.Library() 

    @register.filter(name='has_group') 
    def has_group(user, group_name):
        return user.groups.filter(name=group_name).exists() 
    return render(request, 'index.html', context)

