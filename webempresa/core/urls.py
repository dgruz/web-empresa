from django.urls import path

from core import views as core_views

urlpatterns = [
    path('',core_views.inicio,name="inicio"),
    path('historia/',core_views.historia,name="historia"),
    path('store/',core_views.visitanos,name="visitanos"),
]