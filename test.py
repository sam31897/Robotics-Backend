# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sklearn.decomposition import PCA
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# Create your views here.

featureExtractionPath = "/Users/ashish/Desktop/OpenFace/OpenFace/build/bin/FeatureExtraction"
openFacePath = "someTempPath"

@csrf_exempt
def runOpenFace(videoPath, videoName):
    res = subprocess.check_output([featureExtractionPath, '-f', '/Users/ashish/Downloads/videoplayback.mp4'])
    for line in res.splitlines():
        print(line)
    processedOpenFacePath = "/Users/ashish/Desktop/processed/videoplayback.csv"
    df = pd.read_csv(processedOpenFacePath)
    print(df)
    df_json = df.to_json('temp.json', orient='records', lines=True)
    pca = PCA(n_components=2)

    principalComponents = pca.fit_transform(df)
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

@csrf_exempt
def runOpenPose(request):
    return


runOpenFace("","")