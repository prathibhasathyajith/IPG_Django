from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from . forms import generateHiddenFiles
from . hiddenfields import Allfields
from random import *

def index(request):

    form = generateHiddenFiles()

    context={
        "generatehiddeninputs": form
    }

    return render(request,"index.html",context)


def page1(request):

    return render(request,"page1.html")

def page2(request):

    form = generateHiddenFiles()
    inputs = Allfields();
    context = {
        "merchantId" : inputs.getmid(),
        "dateofregistry" : "2018-08-20",
        "refno" : randint(1, 1000),
        "orderid" : randint(1, 100),
        "generatehiddeninputs": form,
        "url": "http://127.0.0.1:8000/admin",
        "urlipg": "http://localhost:7001/EPIC_IPG/IPGMerchantAddOnServlet"
    }

    return render(request,"page2.html",context)

def page3(request):

    form = generateHiddenFiles()

    context={
        "generatehiddeninputs": form,
        "url": "http://127.0.0.1:8000/admin",
        "urlipg": "http://localhost:7001/EPIC_IPG/IPGMerchantAddOnServlet"
    }

    return render(request,"page3.html",context)