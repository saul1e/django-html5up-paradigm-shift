from django.contrib import admin
from django.urls import path
#from django.views.generic.simple import direct_to_template

# importing views from views..py
from .views import view_index, view_contact_form_success

urlpatterns = [
    path('', view_index),
    path('success/', view_contact_form_success, name='success'),
]