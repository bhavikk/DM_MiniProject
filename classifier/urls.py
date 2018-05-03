from django.urls import path
from . import views

urlpatterns=[
	path('index',views.index,name='index'),
	path('search',views.search,name='search'),
	path('search_form',views.search_form,name='search_form'),
	path('search_form_new',views.search_form_new,name='search_form_new'),
	path('regression',views.regression,name='regression'),
	path('new_form',views.new_form,name='new_form'),

]