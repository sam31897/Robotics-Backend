# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD
import subprocess
=======
from subprocess import call #library for command line calls
>>>>>>> 4b239ba08c63c5e1208ddf6129fce841b43fc561

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