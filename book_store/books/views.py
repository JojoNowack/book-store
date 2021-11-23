from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator
from .models import Articles
from .filters import booksFilter


# Create your views here.

def getdetails(request):
 try:
    template = loader.get_template('products.html')
    id = request.GET['id']
    stud = Articles.objects.get(id=id)
    context = {"stud": stud}
    return HttpResponse(template.render(context,request))
 except:
    id = 3 # 404 Book
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
   
    paginated_filtered_books = Paginator(filtered_books.qs, 20)
    page_number = request.GET.get('page')
    books_page_obj = paginated_filtered_books.get_page(page_number)
    context = {"filtered_books": filtered_books, "title": title, "author": author, "all_articels": all_articels, "books_page_obj": books_page_obj}
    #return HttpResponse(template.render(context,request))
    return render(request,'index.html',context=context)
 except:
    title = ''
    author = ''
    context = {"filtered_books": filtered_books, "title": title, "author": author, "all_articels": all_articels}
    return render(request,'index.html',context=context)



def show_all_books_page(request):
    context = {}
    filtered_books = booksFilter(
        request.GET,
        queryset=Articles.objects.all()
    )


    context = {
             'filtered_books': filtered_books,
              }
    return render(request,'index.html',context=context)




