# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


@csrf_exempt
def uploadVideo(request):
    if request.method != 'POST':
        return JsonResponse({'status': 400, 'message': "Error, please use POST." }, status=400)

    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)

    return {'status': 200,
            'message': "Video uploaded successfully",
            'data': {'filepath': uploaded_file_url}}