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
import random


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
#QRcode Daten empfangen
def qrcode(request):
    if(write_temp_order(request)):
      #response = render(request, 'collection.html',)
      current_user = request.user
      qr = collection.objects.get(user=current_user)   
      qrcode = qr.temp_number
      template = loader.get_template('collection.html')
      context = {"qrcode": qrcode}
      messages.success(request, f"Dein Abholungscode wird generiert...  ") 
      return HttpResponse(template.render(context,request))
    else:
      template = loader.get_template('collection.html')
      context = {"qrcode": False}
      messages.warning(request, f"Du hast momentan keine Bücher zum Abholen") 
      return HttpResponse(template.render(context,request))
      return 
    #return response
#Falls Bücher zum ausleihen vorhanden sind und diese noch nicht in der Bibiliothek abgeholt worden sind
#also book_borrowed =! True, dann soll er alle Bücher mit einem Array in den QR Code schreiben
#Jeder Code ist immer nur einmal verfügbar und wird danach gelöscht.
#Tabelle: collection
def write_temp_order(request):
    try:
     string1 = ''
     isfirst = True
     current_user = request.user
     rdm =random.randint(1000000,9999999)
     all_books = Order.objects.filter(users=current_user.id)
     x2 = len(all_books)
     for x in range(x2):
       if(all_books[x].book_borrowed): # Buch wurde schon augeliehen? --> Nicht in QR Code mitnehmen
         DO_NOTHING
       else:
         if(isfirst):
            string1 = str(all_books[x].books.id)
            isfirst = False
         else:
            string1 = string1 + ","+str(all_books[x].books.id)
     #print(string1)
     collection.objects.filter(user=current_user.id).update(all_orders=string1)
     collection.objects.filter(user=current_user.id).update(temp_number=rdm)
     if(isfirst): #Keine Abholung notwendig
        return False 
     else:
        return True
    except Exception as e:
     PrintException()
     return False
    return

#Nur für Superuser, wenn der Benutzer kein superuser ist, wird er wieder an die Hauptseite weitergeleitet.
#Superuser hat die Möglichkeit einzelne Bücher zu selectieren und den Wert: book_borrowed also Buch abgeholt
#auf True zu setzen und somit hat der Benutzer dann diese Buch ausgehliehen.
#Die Methode hat eine Get und eine Post Methode.
#Bei Post wird die QR Code nummer in einem Link aufgewangen z.B. http://127.0.0.1:8000/order/borrow/?code=23943 <-- Code
#Durch diesen Code sucht man in der Tabelle Collection die ausgeliehenen Bücher und man kann diese dann ausleihen / book_borrowed auf True setzen
def admin_borrow(request):
 if request.user.is_superuser:
    current_user = request.user
    id = request.GET['code']
    if request.method == 'POST':
         buecher = request.POST.getlist('buch[]')
         for i1 in range(10):
           if i1 in range(-len(buecher), len(buecher)):
               #Bücher auf borrow setzen
               #print(buecher)
               order_user = collection.objects.filter(temp_number=id)           
               Order.objects.filter(users=order_user[0].user_id,books=buecher[i1]).update(book_borrowed=1)
               total = Book.objects.filter(id=buecher[i1])
               total_order = total[0].totalorders
               total_order = total_order + 1
               print("total.orders: "+ str(total[0].totalorders))
               Book.objects.filter(id=buecher[i1]).update(totalorders=total_order)
               collection.objects.filter(user=order_user[0].user_id).update(all_orders='')
               #return redirect('admin_order-site')
           else:
               DO_NOTHING
         messages.success(request, f"Aktion erfolgreich durchgeführt.") 
         template = loader.get_template('admin_collection.html')
         context = {"button": False,"success":True}
         return HttpResponse(template.render(context,request))
        #Get Methode zum Anzeigen von den ausgeliehenen Büchern
       
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
      #Bei Fehler --> Abholungscode ist ungültig
       #logger = logging.Logger('catch_all') # POST
       #print(bcolors.FAIL +"WARNUNG: Der Ausleihprozess konnte nicht abgeschlossen werden!" +  bcolors.ENDC)
       #logger.error(bcolors.FAIL +'WARNUNG: '+ str(e) + bcolors.ENDC)
       #PrintException()
       messages.warning(request, f"Abholungscode ist ungültig!  ") 
       context = {"button": False}
       template = loader.get_template('admin_collection.html')
     return HttpResponse(template.render(context,request))
    return redirect('books-site')
 else:
    return redirect('books-site')


#Copy Code from https://stackoverflow.com/questions/14519177/python-exception-handling-line-number/20264059 
#Start 
def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print(bcolors.WARNING + "WARNUNG: IN Zeile: " + str(lineno) + " mit Fehler: "+ bcolors.FAIL + line.strip()  + bcolors.ENDC)
#END 