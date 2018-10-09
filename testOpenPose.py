# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from sklearn.decomposition import PCA
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
# Create your views here.

featureExtractionPath = "./build/examples/openpose/openpose.bin"
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



def runOpenFace(videoPath, videoName, runOpenFace = True):

    #testing
    videoName = "short.mov"
    videoPath = 'examples/media/{}'.format(videoName)
    #run openface on video
    if runOpenFace:
        res = subprocess.check_output([featureExtractionPath, '--video', videoPath, '-write_json', 'openposeOutput'])
        for line in res.splitlines():
            print(line)
        processedOpenFacePath = "/Users/ashish/Desktop/processed/videoplayback.csv"

    videoOutputs = []

    quit = False
    counter = 0
    cwd = os.getcwd()
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




    #need it in format of example, features

    # df = pd.read_csv(processedOpenFacePath)
    # print(df)
    # df_json = df.to_json('temp.json', orient='records', lines=True)
    pca = PCA(n_components=2)

    principalComponents = pca.fit_transform(allExamples)
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



runOpenFace("","")
