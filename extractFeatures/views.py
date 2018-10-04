# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import subprocess
import os



# Create your views here.

featureExtractionPath = "/Users/ashish/Desktop/OpenFace/OpenFace/build/bin/FeatureExtraction"
openFacePath = "someTempPath"

@csrf_exempt
def runOpenFace(request):
    if request.method != 'GET':
        return JsonResponse({'status_code': 400, 'message': "Error, please use GET." }, status=400)

    filename = request.GET.get('filename')
    cwd = os.getcwd()
    res = subprocess.check_output([featureExtractionPath, '-f', '{}/media/{}'.format(cwd, filename)])
    for line in res.splitlines():
        print(line)
    csvFileName =  "{}.csv".format(filename[:-4])
    print(csvFileName)
    processedOpenFacePath = "{}/processed/{}".format(cwd, csvFileName)

    with open(processedOpenFacePath, 'rb') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}'.format(csvFileName)
        return response
    
    return JsonResponse({'status_code': 400, 'message': "Error, openFace failed." }, status=400)

@csrf_exempt
def runOpenPose(request):
    return