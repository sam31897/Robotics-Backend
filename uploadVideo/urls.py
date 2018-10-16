from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^videos/', views.uploadVideo),
    url(r'^uploadOpenFaceCSV/', views.uploadOpenFaceCSV),
    url(r'^uploadOpenPoseCSV/', views.uploadOpenPoseCSV)
]