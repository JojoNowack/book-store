from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author' : 'Kevin Schmidt',
        'title' : 'Mein erstes Programm mit Django',
        'content' : 'Das ist ein kurzer Überblick über das Framework',
        'date_posted' : 'November 04, 2021'
    },
    {
        'author' : 'Carmen Behringer',
        'title' : 'Marketing ist nur Werbung',
        'content' : 'Erläuterung des Marketing Begriffs',
        'date_posted' : 'November 04, 2021'
    }
]
# def loginView(request):
#     return render(request, "login.html",{})

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'account/login.html', context)

def about(request):
    return render(request, 'account/about.html',{'title':'About'})