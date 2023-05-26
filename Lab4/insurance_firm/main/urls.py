from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/
    path('company_branch/<slug:branch>/', company_branch), # http://127.0.0.1:8000/information/1/
    path('insurance_type/<slug:ins_type>/', insurance_type),
    path('client/<slug:client>/', info_client),
    path('insurance_contract/<slug:contract>/', insurance_contract),
    path('object/<slug:i_object>/', info_object),
    path('insurance_agent/<slug:agent>/', insurance_agent)
]