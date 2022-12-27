from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    form=ModelForms()
    d={'form':form}
    if request.method=='POST':
        form_data=ModelForms(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Topic model data inserted')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    form=WebpageForms()
    d={'form':form}
    if request.method=='POST':
        form_data=WebpageForms(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('webpage data inserted sucessfully')


    return render(request,'insert_webpage.html',d)


def insert_AcessRecords(request):
    form=AcessRecordsForms()
    d={'form':form}
    if request.method=='POST':
        form_data=AcessRecordsForms(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('AcessRecodes data will be inserted')
    return render(request,'insert_AcessRecords.html',d)
