from django.urls import path

from msbdev import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.index2, name="index2"),
    # path("resume/", views.resume, name="resume"),
    path("api/submit/", views.submit_form, name="formsubmit"),
    ]
