import logging
from django.db.models.deletion import DO_NOTHING
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.template import loader
from books.models import Book
from .models import collection
from order.models import Order
import linecache
import sys


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

@login_required
def qrcode(request):
    #response = render(request, 'collection.html',)
    current_user = request.user
    qr = collection.objects.get(user=current_user)   
    qrcode = qr.temp_number
    #getsuperuser
    template = loader.get_template('collection.html')
    context = {"qrcode": qrcode}
    messages.success(request, f"Dein Abholungscode wurde generiert.  ") 
    return HttpResponse(template.render(context,request))
    #return response

def admin_borrow(request):
 if request.user.is_superuser:
    current_user = request.user
    if request.method == 'POST':
         buecher = request.POST.getlist('buch[]')
         for i1 in range(10):
           if i1 in range(-len(buecher), len(buecher)):
               #Bücher auf borrow setzen
               print(buecher)
               Order.objects.filter(users=current_user.id,books=buecher[i1]).update(book_borrowed=1)
               collection.objects.filter(user=current_user.id).update(all_orders='')
               #return redirect('admin_order-site')
           else:
               DO_NOTHING
         messages.success(request, f"Aktion erfolgreich durchgeführt.") 
         template = loader.get_template('admin_collection.html')
         context = {"button": False,"success":True}
         return HttpResponse(template.render(context,request))
        
    if request.method == 'GET':
     all_ordered_books = {}   
     try:
      id = request.GET['code'] 
      current_order = collection.objects.get(temp_number=id)
      txt = str(current_order.all_orders)
      x = txt.split(",")
      #print(x[1])
      for i in range(10):
        #print(i)
        if i in range(-len(x), len(x)):
           all_ordered_books[i] = x[i]
        else:
           all_ordered_books[i] = 0
      template = loader.get_template('admin_collection.html')
      #Max 10 Orders available
      all_books = Book.objects.filter(id__in=[all_ordered_books[0],all_ordered_books[1],all_ordered_books[2],all_ordered_books[3],all_ordered_books[4],all_ordered_books[5],all_ordered_books[6],all_ordered_books[7],all_ordered_books[8],all_ordered_books[9]])
      #print(str(all_books))
      context = {"all_books":all_books}
      return HttpResponse(template.render(context,request))  
     except Exception as e:
       logger = logging.Logger('catch_all') # POST
       print(bcolors.FAIL +"WARNUNG: Der Ausleihprozess konnte nicht abgeschlossen werden!" +  bcolors.ENDC)
       logger.error(bcolors.FAIL +'WARNUNG: '+ str(e) + bcolors.ENDC)
       PrintException()
       messages.warning(request, f"Abholungscode ist ungültig!  ") 
       context = {"button": False}
       template = loader.get_template('admin_collection.html')
     return HttpResponse(template.render(context,request))
    return redirect('books-site')

def admin_borrow_view(request):
     template = loader.get_template('admin_collection.html')
     context = {}
     return HttpResponse(template.render(context,request))

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print(bcolors.WARNING + "WARNUNG: IN Zeile: " + str(lineno) + " mit Fehler: "+ bcolors.FAIL + line.strip()  + bcolors.ENDC)

def finish_orders(request):
     if request.method == 'POST':
         print("yes") 
     return