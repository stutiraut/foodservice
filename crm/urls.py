from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'crm'
urlpatterns = [

    path('', views.customer_list, name='customer_list'),

]
