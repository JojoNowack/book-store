from django.shortcuts import render

# Create your views here.

def loginView(request):
    if (request.GET.get('mybtn')):
       print( request.GET.get('mytextbox'))
    return render(request, "login.html",{})