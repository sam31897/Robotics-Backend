# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import subprocess

# Create your views here.

featureExtractionPath = "somePathHere"
openFacePath = "someTempPath"

@csrf_exempt
def runOpenFace(videoPath, videoName):
    res = subprocess.call([featureExtractionPath], ["-f"], [videoPath])
    processedOpenFacePath = openFacePath + "/processed" + videoName + ".csv"
    
    return 

@csrf_exempt
def runOpenPose(request):
    return