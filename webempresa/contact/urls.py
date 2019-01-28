from django.urls import path

from contact import views as core

urlpatterns = [
    path('',core.contact,name="contact"),
]