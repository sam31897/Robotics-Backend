# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def runOpenFace(request):
    return 

@csrf_exempt
def runOpenPose(request):
    return