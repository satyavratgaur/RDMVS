from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from django.conf import settings

from upload.models import Uploads
from login.forms import UserAuthentication
import os


def uploads_page(request): 
    return render(request, 'upload.html')

def file_upload(request):
    target = settings.DOWNLOAD_ROOT

    if not os.path.isdir(target):
        os .mkdir(target)

    # print("==>",request.FILES)
    file = request.FILES['file']
    target = os.path.join(target, file.name)
    print(target)
    fout = open(target, 'wb+')
    for chunk in file.chunks():
        fout.write(chunk)
    fout.close()

    return HttpResponseRedirect('/pvrl/s-uploads')

    
