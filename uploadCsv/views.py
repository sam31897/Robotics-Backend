# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


# Create your views here.
@csrf_exempt
def uploadCSV(request):
    if request.method != 'POST':
        return JsonResponse({'status_code': 400, 'message': "Error, please use POST." }, status=400)

    cwd = os.getcwd()
    myfile = request.FILES['myCSV']
    libraryType = request.POST.get('type')
    print(libraryType)
    path = ""
    if libraryType == "openface":
        path = "{}/processed/".format(cwd)
    else:
        path = "{}/openPoseCSV/".format(cwd)
    fs = FileSystemStorage(location=path)
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)

    return JsonResponse({'status_code': 200,
            'message': "Video uploaded successfully",
            'data': {'filepath': uploaded_file_url}})
