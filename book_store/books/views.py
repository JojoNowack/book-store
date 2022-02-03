
from typing import Reversible
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt, csrf_protect



from .models import Book, Category
from .filters import booksFilter, booksFilterwithGenre
from order.models import Order
from account.models import Profile
from django.contrib.auth.models import User
import logging
from django.utils import timezone
import pytz
from datetime import datetime, date, time, timedelta
from django.urls import reverse

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

# Diese Funktion wird für das Anzeigen der einzelnen Büchern in z.B. http://127.0.0.1:8000/books/products/?title=harry%20potter%20und%20der%20gefangene%20von%20askaban&id=4
# verwendet.
# Sie hat eine Get und eine Post Methode
# Get = anzeigen des Buches auf products.html
# Post = Bestellprozess in products.html mit allen Fehlermeldungen
@csrf_exempt
def getdetails(request):
       @csrf_protect
       
       def protected_path(request):
            print("ERROR CSRF_PROTECT IN BOOKS.VIEWS.PY")
       
       current_user = request.user
       showalert = 0 
       
            
       try:   
          
          if request.method == 'GET':
             #Get Methode für das reine anzeigen der Bücher
               
                try:
                #Falls der Wert Status übergeben wird
                    status = request.GET['status'] 
                    orderdata = Order.objects.all()
                    template = loader.get_template('products.html')
                    id = request.GET['id']          
                    currentbook = Book.objects.get(id=id)
                    all_articels = Book.objects.all()
                    context = {"currentbook": currentbook,"all_articels":all_articels,"orderdata":orderdata,"status": status}     
                    return HttpResponse(template.render(context,request))
                except:
                   {}
                try:
                #Falls der Wert Status nicht übergeben wird 
                    orderdata = Order.objects.all()   
                    template = loader.get_template('products.html')
                    id = request.GET['id']          
                    currentbook = Book.objects.get(id=id)
                    all_articels = Book.objects.all()
                    # Kategorie bekommen
                    Kategorie = Book.genre.through.objects.filter(book_id=id)
                    all_categories = Category.objects.all()               
                    context = {"currentbook": currentbook,"all_articels":all_articels,"orderdata":orderdata,"Kategorie":Kategorie,"all_categories":all_categories}     
                    return HttpResponse(template.render(context,request))
                except Exception as e:
                    #Buch wurde nicht gefunden und Buch mit ID 1 wird stattdessen ausgegeben
                    #Fehlermeldung falls das Buch nicht gefunden wurde
                    #Buch mit ID 1 wird ausgegeben, das wird immer angezeigt, falls etwas nicht gefunden wird Buch mit ID 1 = Buch 404
                    logger = logging.Logger('catch_all')
                    logger.error(bcolors.FAIL +'WARNUNG: '+ str(e) + bcolors.ENDC)
                    id = 1 # 404 Book
                    currentbook = Book.objects.get(id=id)
                    all_articels = Book.objects.all()
                    context = {"currentbook": currentbook,"all_articels":all_articels}
                    print(bcolors.WARNING +"ACHTUNG: Fehler in books.views(getdetails) - Buch wurde nicht gefunden - Buch mit ID: "+ str(id) +" - "+ str(currentbook) +" wurde ausgegeben"+  bcolors.ENDC)
                    return HttpResponse(template.render(context,request))
          #@login_required
          if request.method == 'POST':
           #Post methode --> Bestellprozess
           #print("POST!!!!!")
           
           BuchID = request.POST.getlist('buch[]') 
           buch = Book.objects.get(id=BuchID[0]) 
           benutzer = User.objects.get(id=current_user.id)
           order_from_user = Order.objects.filter(users=current_user.id)
           ids    = order_from_user.values_list('books', flat=True)
           all_borrowdates_from_user = order_from_user.values_list('return_date', flat=True)
           user_has_borrowed = order_from_user.values_list('book_borrowed', flat=True)

           # Hat der Benutzer ein anderes Buch abgeholt und dessen Abgabe überschritten?
           if(book_over_time(all_borrowdates_from_user,current_user.id,user_has_borrowed) == False):
                 return HttpResponseRedirect('?title='+buch.title+'&id='+str(buch.id)+'&status=4')
                 #Fehler Status 4 --> Abgabe überschritten
           else:
                if int(BuchID[0]) in ids: #Buch wurde schon ausgeliehen
                  print(bcolors.WARNING +"WARNUNG: User: "+ str(benutzer) + " wollte Buch: "+ str(buch) + " ein weiteres mal ausleihen!" + bcolors.ENDC)
                  return HttpResponseRedirect('?title='+buch.title+'&id='+str(buch.id))
                  #Fehler Benutzer versucht das gleiche Buch nochmal auszuleihen
                else: #Buch ausleihen
                  if(countmaxbooks(request)):
                      print(bcolors.WARNING+ "ACHTUNG: Benutzer mit ID: "+ str(current_user) + " hat die maximale Anzahl an Büchern erreicht!"+ bcolors.ENDC)
                      return HttpResponseRedirect('?title='+buch.title+'&id='+str(buch.id)+'&status=5')     

                  if(buch.isavailable):
                   currentDate = date.today()
                   returnDate = currentDate + timedelta(days=buch.ausleihtage)
                   o = Order.objects.create(books=buch,users=benutzer,borrow_date=currentDate,return_date=returnDate,book_borrowed=False)
                   o.save()
                   
                   print(bcolors.OKGREEN +"Buch ID: " + str(BuchID[0]) +" wurde von ID: " +str(current_user.id)+" ausgeliehen"+ bcolors.ENDC)
                   return HttpResponseRedirect('?title='+buch.title+'&id='+str(buch.id)+'&status=success')
                   #Buch erfolgreich ausgeliehen
                  else:
                   print(bcolors.OKGREEN +"Buch ID: " + str(BuchID[0]) +" konnte nicht " +str(current_user.id)+" ausgeliehen - Kein Buch vorhanden!"+ bcolors.ENDC)
                   #Buch nicht vorhanden+
                   return HttpResponseRedirect('?title='+buch.title+'&id='+str(buch.id)+'&status=failed')


       except Exception as e:
           #Unerwarteter Fehler im Gesamten Bestellprozess
           #z.B. ist ein unerklärlichen Gründen der Bestand des Buches auf unter 0 gesprungen und es 
           # konnte trotzdem ausgeliehen werden, dann triggert die Datenbank mit einem Trigger     
           logger = logging.Logger('catch_all') 
           print(bcolors.FAIL +"WARNUNG: Der Ausleihprozess konnte nicht abgeschlossen werden!" +  bcolors.ENDC)
           logger.error(bcolors.FAIL +'WARNUNG: '+ str(e) + bcolors.ENDC)
           PrintException()
           return HttpResponseRedirect('?title='+buch.title+'&id='+str(buch.id)+'&status=error')

# Maximale Bücher des Users zählen, ist er über 10 --> return false und beende den Prozess mit einer Alert Message
def countmaxbooks(request):
    current_user = request.user
    test = Order.objects.filter(users=current_user)
    x = len(test)
    # 10 Bücher dürfen maximal ausgeliehen werden
    # könnte man in neueren Versionen auch aus dem Trigger auslesen
    if x >= 10:
      return True
    else:
     return False



def book_over_time(borrowdates,current_user,user_has_borrowed):
    for i in range(len(borrowdates)):
       #date_time_obj = datetime.strptime(str(borrowdates[i]),'%y/%m/%d %H:%M:%S')
       currentDate = date.today()
       #currentDate_timezone = timezone.make_aware(currentDate)
       #print(currentDate_timezone)
       if currentDate <= borrowdates[i]:
          {}
       else:
            # ist das buch überhaupt abgeholt worden --> borrowed_book auf True?
            if ( user_has_borrowed[i] == False):
              return True
            else:
              print(bcolors.WARNING+ "ACHTUNG: Abgabe wurde überschritten, Benutzer mit ID: "+ str(current_user) + " kann keine weiteren Bücher mehr ausleihen!"+ bcolors.ENDC)
              return False
    return True
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
#End 


# Zum anzeigen der Bücher in der Main Page
# Werte werden durch einen Context dem template index.html übergeben
def booksmainpage(request):
   print('Bücher werden angezeigt')
   try:
        genre = request.GET['genre'] # Filter mit Genre
        #Für Genre haben wir ein eigenen Filter (direkt ober erweiterte suche), wenn dieser ausgewählt 
        # ist muss man den wert genre abfangen und diesen in die Form (erweiterte suche) eintragen
        # Die Form übergibt dann den Wert weiter für die Filterung
        # Da sonst zu viele Werte in der Form stehen, haben wir 2 Filter erstellt, einmal ohne genre und einmal mit genre, aber ersetzen das Dropdown menu.
        # So bleibt die Form immer gleich.
        filtered_books = booksFilterwithGenre(
        request.GET,
        queryset=Book.objects.all()
        )
        all_articels = Book.objects.all()
   except: # Filter ohne Genre
        filtered_books = booksFilter(
        request.GET,
        queryset=Book.objects.all()
        )

        all_articels = Book.objects.all()
        #title = request.GET['title'].lower()
   finally:
        paginated_filtered_books = Paginator(filtered_books.qs, 10) # maximale bücher anzeigen --> hier sind es 10 kann man aber immer frei wählen
        page_number = request.GET.get('page')
        books_page_obj = paginated_filtered_books.get_page(page_number)
        categories = Category.objects.all()
        context = {"filtered_books": filtered_books, "all_articels": all_articels, "books_page_obj": books_page_obj,"categories": categories}
        #return HttpResponse(template.render(context,request))  
        return render(request,'index.html',context=context)



