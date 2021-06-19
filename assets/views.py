from os import name, truncate
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.conf import settings
from django.conf.urls import url
import os
#render to pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

#My Models
from .models import DeliveryAsset,Asset,Delivery,Location,Logo
# Create your views here.
import json

import datetime
from django.http import JsonResponse
def assets(request):
    if request.user.is_authenticated:
        branch=Location.objects.all()
        staff=request.user.staff
        delivery, dispatched=Delivery.objects.get_or_create(staff=staff, dispatched=False)
        deliveryList=Delivery.objects.filter(staff=staff, dispatched=True)
        # currentDelivery=delivery.deliveryNo
        asset=delivery.deliveryasset_set.all()
        delivery.deliveryNo='DEL-'+ delivery.key1
        delivery.save()
        deliveryitems=delivery.get_delivery_items_no
        # deliveryItem2, dispatched = DeliveryAsset.objects.filter()
        deliveryitemsss=delivery.deliveryasset_set.all()
    assets =Asset.objects.filter(location=request.user.staff.location, transit=False)
    context={
        'branch':branch,
        'delivery':delivery, 
        'staff':staff,
        'deliveryList':deliveryList,
        'deliveryitemsss':deliveryitemsss,
        'assets':assets,
        'deliveryitems':deliveryitems
        }
    return render(request, 'assets/index.html', context)

def updateAsset(request):
    staff=request.user.staff
    staff.save()
    data=json.loads(request.body)
    assetId=data['assetId']
    action=data['action']
    print('Action:', action)
    print('Product:', assetId)
    staff=request.user.staff
    asset=Asset.objects.get(id=assetId)
    delivery, dispatched=Delivery.objects.get_or_create(staff=staff, dispatched=False)
    deliveryItem, dispatched = DeliveryAsset.objects.get_or_create(delivery=delivery,asset=asset)
    
    if action == 'add':
        deliveryItem.quantity = (deliveryItem.quantity + 1)
        asset.transit = True
    elif action == 'remove':
        deliveryItem.quantity = (deliveryItem.quantity - 1)
    deliveryItem.save()
    asset.save()
    if deliveryItem.quantity <= 0:
        deliveryItem.delete()
        asset.transit = False

    return JsonResponse('Item was Added', safe=False)
 
def processResponse(request, *args, **kwargs ):
    # pk = kwargs.get('pk')
    # data=json.loads(request.body)
    if request.user.is_authenticated:
        staff=request.user.staff
        delivery, dispatched=Delivery.objects.get_or_create(staff=staff, dispatched=False)
        delivery.dispatched =True
        delivery.date_dispatched=datetime.datetime.now()
        delivery.fromLocation=request.user.staff.location
        #get toLocation
        delivery.save()
    return redirect('assets:index')


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
                    path=result[0]
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
        staff=request.user.staff
        delivery=Delivery.objects.filter(staff=staff, dispatched=True,pk=pk)
        logo =Logo.objects.first()
        context={
            'delivery':delivery,
            'logo':logo
            }
        template_path='assets/delivery.html'
        response = HttpResponse(content_type='application/pdf')
        
        filename='DEL-'+ pk.zfill(6)
        response['Content-Disposition']="filename=%s.pdf"%(filename)
        # response['Content-Disposition']="filename=ali.pdf"
        template= get_template(template_path)
        html=template.render(context)

    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response,  link_callback=link_callback
    )
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response 