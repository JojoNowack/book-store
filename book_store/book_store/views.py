import logging
import sys
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import linecache
# Create your views here.

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def customhandler404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response

def customhandler500(request):
    current_user = request.user
    response = render(request, '500.html',)
    response.status_code = 500
    exc_type, exc_obj, tb = sys.exc_info()
    print(bcolors.FAIL+"User: "+str(current_user)+" hat folgende Fehlermeldung ausgelöst= "+str(exc_obj)+bcolors.ENDC)
    context = {"error_msg": str(exc_obj)}
    return render(request, '500.html', context)

def faq(request):
    return render(request, 'faq.html')
