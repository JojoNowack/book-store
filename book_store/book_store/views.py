from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def customhandler404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response

def customhandler500(request):
    response = render(request, '500.html',)
    response.status_code = 500
    return response

