from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.conf import settings
from django.conf.urls import url
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import Q

# system
import json
import datetime
import os
from os import name, truncate

# render to pdf
from xhtml2pdf import pisa

# Account
from allauth.account.decorators import login_required

# My Models
from .models import DeliveryAsset, Asset, Delivery, Location, Logo
from .forms import AssetForm

@login_required
def deliveries(request):
    if request.user.is_authenticated:
        # staff=request.user.staff
        deliveryList = Delivery.objects.filter(
            dispatched=True).order_by('id').reverse()
        paginator = Paginator(deliveryList, 2)
        page_number = request.GET.get('page')
        pages = paginator.get_page(page_number)

    context = {
        'pages': pages,
    }
    return render(request, 'assets/deliveries.html', context)


@login_required
def assets(request):
    if request.user.is_authenticated:
        branch = Location.objects.all()
        staff = request.user.staff
        delivery, dispatched = Delivery.objects.get_or_create(
            staff=staff, dispatched=False)
        deliveryList = Delivery.objects.filter(
            staff=staff, dispatched=True).order_by('id').reverse()
        # paginate deliveries
        paginator = Paginator(deliveryList, 5)
        page_number = request.GET.get('page')
        pages = paginator.get_page(page_number)
       
        # currentDelivery=delivery.deliveryNo
        asset = delivery.deliveryasset_set.all()
        delivery.deliveryNo = 'DEL-' + delivery.key1
        delivery.save()
        deliveryitems = delivery.get_delivery_items_no
        acc = Asset.objects.filter(accessory=True)
        # deliveryItem2, dispatched = DeliveryAsset.objects.filter()
        deliveryitemsss = delivery.deliveryasset_set.all()
        # Search Assets
        url_parameter = request.GET.get("q")
        
        if url_parameter: 
            assets = Asset.objects.filter(
                barcode__icontains= url_parameter,
                location=request.user.staff.location,
                transit=False
                )
        else:
            assets = Asset.objects.filter(location=request.user.staff.location, transit=False) | Asset.objects.filter(accessory=True)
            
    form =AssetForm()
    if request.method =="POST":
        form=AssetForm(request.POST)
        if form.is_valid():
            fs=form.save(commit =False)
            fs.location= request.user.staff.location
            fs.save()
            return redirect('/assets')
        else: 
            return(HttpResponse("An error occurred"))
    context = {
        'form':form,
        'pages': pages,
        'branch': branch,
        'delivery': delivery,
        'staff': staff,
        'deliveryList': deliveryList,
        'deliveryitemsss': deliveryitemsss,
        'assets': assets,
        'deliveryitems': deliveryitems
    }
    return render(request, 'assets/index.html', context)


@login_required
def updateAsset(request):
    staff = request.user.staff
    staff.save()
    data = json.loads(request.body)
    assetId = data['assetId']
    action = data['action']
    print('Action:', action)
    print('Product:', assetId)
    staff = request.user.staff
    asset = Asset.objects.get(id=assetId)
    delivery, dispatched = Delivery.objects.get_or_create(
        staff=staff, dispatched=False)
    deliveryItem, dispatched = DeliveryAsset.objects.get_or_create(
        delivery=delivery, asset=asset)

    if action == 'add':
        deliveryItem.quantity = (deliveryItem.quantity + 1)
        if asset.accessory != True:
            asset.transit = True
         
    elif action == 'remove':
        deliveryItem.quantity = (deliveryItem.quantity - 1)
    deliveryItem.save()
    asset.save()
     
    if deliveryItem.quantity <= 0:
        deliveryItem.delete()
        asset.transit = False
    asset.save()

    # return redirect('assets:index')
    return JsonResponse('Item was Added', safe=False)


@login_required
def processResponse(request, *args, **kwargs):
    # pk = kwargs.get('pk')
    if request.user.is_authenticated:
        data=json.loads(request.body)
        branch = data['branch']
        loc=Location.objects.get(pk=branch)

        # asset =Delivery.get_delivery_assets()
        staff = request.user.staff

        delivery, dispatched = Delivery.objects.get_or_create(
            staff=staff, dispatched=False)
        # deliveryitemsss = delivery.deliveryasset_set.all()
        # deliveryitemsss = delivery.deliveryasset_set.all()
        # deliveryItem, dispatched = DeliveryAsset.objects.get_or_create(
        # delivery=delivery, asset=deliveryitemsss)

        # x = Asset.objects.get(pk=deliveryitemsss)
        # deliveryItem = DeliveryAsset.objects.get(
        # delivery=delivery)

        delivery.dispatched = True
        delivery.toLocation=loc
        delivery.date_dispatched = datetime.datetime.now()
        delivery.fromLocation = request.user.staff.location

        # get toLocation
        
        delivery.save()
        # x.location =loc
        # x.save()
    return JsonResponse('Item was Added', safe=False)
    # return redirect('assets:index')



def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    print(path)
    return path



def deliveries_pdf(request, *args, **kwargs):
    pk = kwargs.get('pk')
    if request.user.is_authenticated:
        staff = request.user.staff
        delivery = Delivery.objects.filter(staff=staff, dispatched=True, pk=pk)
        logo = Logo.objects.first()
        context = {
            'delivery': delivery,
            'logo': logo
        }
        template_path = 'assets/delivery.html'
        response = HttpResponse(content_type='application/pdf')

        filename = 'DEL-' + pk.zfill(6)
        response['Content-Disposition'] = "filename=%s.pdf" % (filename)
        # response['Content-Disposition']="filename=ali.pdf"
        template = get_template(template_path)
        html = template.render(context)

    # create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response,  link_callback=link_callback
    )
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#create a view to issue an asset to a User
# 1. select User,dept,Asset and Issue.. Create table to maintain Asset Issues.

#Create View to receive Asset
