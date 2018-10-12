from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^runVisualizationOpenFace/', views.runVisualizationOpenFace),
     url(r'^runVisualizationOpenPose/', views.runVisualizationOpenPose),
]