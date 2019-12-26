from django.urls import path

from msbdev import views

urlpatterns = [
    path("", views.index, name="index"),
    path("formsubmit/", views.formsubmit, name="formsubmit"),
    ]
