# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pandas
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import json

# Create your views here.

@csrf_exempt
def runVisualizationOpenFace(request):
    if request.method != 'GET':
        return JsonResponse({'status_code': 400, 'message': "Error, please use GET." }, status=400)

    cwd = os.getcwd()
    filename = request.GET.get('fileName')


    split = filename.split('.')
    csvFileName = split[0] + '.csv'

    processedOpenFacePath = "{}/processed/{}".format(cwd, csvFileName)
    df = pd.read_csv(processedOpenFacePath)
    df_json = df.to_json('temp.json', orient='records', lines=True)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(df)
    principalComponentsList = principalComponents.tolist()
    principalComponentsJson = json.dumps(principalComponentsList)
    print(principalComponentsJson)    
    return JsonResponse({'status_code': 200, 'data': principalComponentsJson }, status=200) 

@csrf_exempt
def runVisualizationOpenPose(request):
    if request.method != 'GET':
        return JsonResponse({'status_code': 400, 'message': "Error, please use GET." }, status=400)

    cwd = os.getcwd()
    filename = request.GET.get('fileName')


    split = filename.split('.')
    csvFileName = split[0] + '.csv'

    processedOpenPosePath = '{}/openPoseCSV/{}.csv'.format(cwd, filename[:-4])
    df = pd.read_csv(processedOpenPosePath)
    df_json = df.to_json('temp.json', orient='records', lines=True)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(df)
    principalComponentsList = principalComponents.tolist()
    principalComponentsJson = json.dumps(principalComponentsList)
    print(principalComponentsJson)    
    return JsonResponse({'status_code': 200, 'data': principalComponentsJson }, status=200) 










































