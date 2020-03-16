from django.urls import path

from msbdev import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/submit/", views.submit_form, name="formsubmit"),
    ]
