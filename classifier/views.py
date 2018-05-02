from django.shortcuts import render
from django.http import HttpResponse
from .modules.test import RandomForest
from .modules.test import NaiveBayes
from .modules.test import KNN

# Create your views here.

def index(request):
    return HttpResponse('Hello from post')

def search_form(request):
    return render(request, 'classifier/form.html')

def search(request):
    # message="empty"
    # print(request.GET)
    if 'search' in request.GET:
        if 'Classify' in request.GET:
            if request.GET['Classify'] == 'naives':
                print('here1')
                message = NaiveBayes(request.GET['search'])
            if request.GET['Classify'] == 'RandomForest':
                message = RandomForest(request.GET['search'])
            
            if request.GET['Classify'] == 'KNN':
                message = KNN(request.GET['search'])
        else:
            message = "No method selected"
    else:
        message = 'You submitted an empty form.'
    return render(request,"classifier/results_view.html",{"result":message})
