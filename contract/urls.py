from django.urls import path
from .views import *

urlpatterns = [
    path('', contract_json, name='contract_json'),
    path('contract_json_payment/<slug:slug>/', contract_json_payment, name='contract_json_payment'),
    path('contract_json_detail/<slug:slug>/', contract_json_detail, name='contract_json_detail'),
    path('ajax-posting/', ajax_posting, name='ajax_posting'),
]
