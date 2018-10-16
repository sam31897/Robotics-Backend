# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


@csrf_exempt
def uploadVideo(request):
    # call runOpenFace
    if request.method != 'POST':
        return JsonResponse({'status_code': 400, 'message': "Error, please use POST." }, status=400)

    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)

    return JsonResponse({'status_code': 200,
            'message': "Video uploaded successfully",
            'data': {'filepath': uploaded_file_url}})


@csrf_exempt
def uploadOpenFaceCSV(request):
    if request.method != 'POST':
        return JsonResponse({'status_code': 400, 'message': "Error, please use POST." }, status=400)

    print("here")
    cwd = os.getcwd()
    myfile = request.FILES['myCSV']

    path = "{}/processed/".format(cwd)
    fs = FileSystemStorage(location=path)
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)

    return JsonResponse({'status_code': 200,
            'message': "Video uploaded successfully",
            'data': {'filepath': uploaded_file_url}})


@csrf_exempt
def uploadOpenPoseCSV(request):
    if request.method != 'POST':
        return JsonResponse({'status_code': 400, 'message': "Error, please use POST." }, status=400)

    print("here")
    cwd = os.getcwd()
    myfile = request.FILES['myCSV']

    path = "{}/openPoseCSV/".format(cwd)
    fs = FileSystemStorage(location=path)
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)

    return JsonResponse({'status_code': 200,
            'message': "Video uploaded successfully",
            'data': {'filepath': uploaded_file_url}})