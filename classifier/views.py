from django.shortcuts import render
from django.http import HttpResponse
from .modules.test import RandomForest
from .modules.test import NaiveBayes
from .modules.test import regression1
from .modules.test import KNN

# Create your views here.

def index(request):
    return HttpResponse('Hello from post')

def search_form(request):
    return render(request, 'classifier/form.html')

def search_form_new(request):
    return render(request, 'classifier/form_new1.html')

def new_form(request):
    return render(request, 'classifier/new_form.html')

def regression(request):
    message=regression1(request.GET)
    print(message)    
    return render(request,"classifier/result_view.html",{"result":message})

def search(request):
    # message="empty"
    print(request.GET)
    if 'search' in request.GET:
        if 'Classify' in request.GET:
            if request.GET['Classify'] == 'naives':
                # print('here1')
                message = NaiveBayes(request.GET['search'])
            if request.GET['Classify'] == 'RandomForest':
                message = RandomForest(request.GET['search'])
            
            if request.GET['Classify'] == 'KNN':
                message = KNN(request.GET['search'])
        else:
            message = "No method selected"
    else:
        message = 'You submitted an empty form.'
    return render(request,"classifier/result_view.html",{"result":message})
