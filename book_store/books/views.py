from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Articles
from .filters import booksFilter


# Create your views here.

def getdetails(request):
    template = loader.get_template('products.html')
    id = request.GET['id']
    stud = Articles.objects.get(id=id)
    context = {"stud": stud}
    return HttpResponse(template.render(context,request))


def booksmainpage(request):
 try:
    context = {}
    filtered_books = booksFilter(
        request.GET,
        queryset=Articles.objects.all()
    )
    all_articels = Articles.objects.all()
    template = loader.get_template('index.html')
    title = request.GET['title'].lower()
    author = request.GET['author'].lower()
    context = {"filtered_books": filtered_books, "title": title, "author": author, "all_articels": all_articels}
    return HttpResponse(template.render(context,request))
 except:
    title = ''
    author = ''
    context = {"filtered_books": filtered_books, "title": title, "author": author, "all_articels": all_articels}
    return HttpResponse(template.render(context,request))



def show_all_books_page2(request):
    context = {}
    filtered_books = booksFilter(
        request.GET,
        queryset=Articles.objects.all()
    )


    context = {
             'filtered_books': filtered_books,
              }
    return render(request,'index.html',context=context)


def show_all_books_page(request):
    context = {}
    filtered_books = booksFilter(
        request.GET,
        queryset=Articles.objects.all()
    )
    title = request.GET['title']
    author = request.GET['author']
    all_articels = Articles.objects.all()
    context = {"filtered_books": filtered_books, "title": title, "author": author, "all_articels": all_articels}

    return render(request,'index.html',context=context)




