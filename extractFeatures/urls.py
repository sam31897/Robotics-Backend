from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^runOpenFace/', views.runOpenFace),
    url(r'^runOpenPose/', views.runOpenPose),
    url(r'^describeData/', views.describeData)
]
