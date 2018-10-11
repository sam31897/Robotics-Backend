# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import subprocess
import os
import pandas as pd
import json



# Create your views here.

featureExtractionPath = "/Users/ashish/Desktop/OpenFace/OpenFace/build/bin/FeatureExtraction"
openFacePath = "someTempPath"

def getVideoNumber(counter):
    vidNum = ""
    strCounter = str(counter)
    for i in range(12):
        if i >= 12 - len(strCounter):
            vidNum = vidNum + strCounter[len(strCounter) - (11-i) - 1]
        else:
            vidNum = vidNum + "0"

    return vidNum

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
    request.session['csvFileName'] = csvFileName
    print(csvFileName)
    processedOpenFacePath = "{}/processed/{}".format(cwd, csvFileName)

    with open(processedOpenFacePath, 'rb') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}'.format(csvFileName)
        return response
    
    return JsonResponse({'status_code': 400, 'message': "Error, openFace failed." }, status=400)

@csrf_exempt
def runOpenPose(request):

    if request.method != 'GET':
        return JsonResponse({'status_code': 400, 'message': "Error, please use GET." }, status=400)

    cwd = os.getcwd()
    videoPath = '{}/media/{}'.format(cwd, videoName)
    #run openface on video
    videoName = request.GET.get('filename')
    res = subprocess.check_output([featureExtractionPath, '--video', videoPath, '-write_json', 'openposeOutput'])
    for line in res.splitlines():
        print(line)
    processedOpenFacePath = "/Users/ashish/Desktop/processed/videoplayback.csv"

    videoOutputs = []

    quit = False
    counter = 0
    
    #loop through all of the jsons and load them in
    while quit != True:
        #check to see if the file exists
        videoNumber = getVideoNumber(counter)
        newFileName = "{}_{}_keypoints.json".format(videoName[:-4], videoNumber)
        newPath = "{}/openposeOutput/{}".format(cwd, newFileName)
        print(newPath)
        exists = os.path.isfile(newPath)
        if exists:
            with open(newPath, 'r') as f:
                newJson = json.load(f)
                videoOutputs.append(newJson)
        else:
            quit = True
        counter = counter + 1
    
    allExamples = []
    for myJson in videoOutputs:
        #print(myJson["people"])
        combinedFeatures = []
        for key in myJson["people"][0]:
            #print("el {}".format(myJson["people"][0][key]))
            for element in myJson["people"][0][key]:
                combinedFeatures.append(element)
        allExamples.append(combinedFeatures)

    df = pd.DataFrame(allExamples)
    openPoseCsv = df.to_csv()
    response = HttpResponse(openPoseCsv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(videoName)
    return response
