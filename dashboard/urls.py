from django.urls import path

from .import views
from .dash_app import app

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
     path('sales/', app.run_server, name='sales_comparison'),
]
