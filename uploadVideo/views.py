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

    
    return