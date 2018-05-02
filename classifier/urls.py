from django.urls import path
from . import views

urlpatterns=[
	path('index',views.index,name='index'),
	path('search',views.search,name='search'),
	path('search_form',views.search_form,name='search_form'),
]