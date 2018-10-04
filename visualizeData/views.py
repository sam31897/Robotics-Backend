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

# Create your views here.

@csrf_exempt
def runVisualization(request):
    if request.method != 'GET':
        return JsonResponse({'status_code': 400, 'message': "Error, please use GET." }, status=400)

    cwd = os.getcwd()
    csvFileName = request.session["csvFileName"]
    processedOpenFacePath = "{}/processed/{}".format(cwd, csvFileName)
    df = pd.read_csv(processedOpenFacePath)
    print(df)
    df_json = df.to_json('temp.json', orient='records', lines=True)
    pca = PCA(n_components=2)

    principalComponents = pca.fit_transform(df)
    print(principalComponents)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('OpenFace Visualization', fontsize = 20)
    targets = ['OpenFace']
    ax.scatter(principalDf.loc[:,'principal component 1'] , principalDf.loc[:, 'principal component 2'] , c = 'r' , s = 50)
    ax.legend(targets)
    ax.grid()
    plt.show()

    #file = open("testfile.text", "w")
    #file.write(df_json)
    #file.close()
    return 