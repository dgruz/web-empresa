from django.urls import path

from services import views as core_services

urlpatterns = [
    path('servicios/',core_services.servicios,name="servicios"),
    
]