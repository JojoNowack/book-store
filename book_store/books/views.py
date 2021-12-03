
from typing import Reversible
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt, csrf_protect



from .models import Book
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

# Create your views here.
@csrf_exempt
def getdetails(request):
       @csrf_protect
       
       def protected_path(request):
            print("ERROR CSRF_PROTECT IN BOOKS.VIEWS.PY")
      
       current_user = request.user
       showalert = 0 
       # ToDo 
       # [x]Schauen ob man über der Zeit liegt
       # [x]ausleihdatum < datetime.today()
       # []Mehr als 3 Bücher ausgeliehen? --> Trigger?
       # [x]neue Funktion?
       # [x]evtl ausleihen rückgängig?
       # [X]abgeholt value?
       # [x]for all books loop
       # [x]save
       # [x]Timezone support
       # []Abgebe überschritten und Datum richtig anzeigen
       # []bei zurück Post nicht nochmal senden?
       # [x]user muss eingelogt werden
            
       try:   
          
          if request.method == 'GET':
             
                print("GETTTT!!")
                id2 = request.GET['status']
            
          if request.method == 'POST':
           print("POST!!!!!!")
           print(bcolors.HEADER + "STARTING" + bcolors.ENDC)
           BuchID = request.POST.getlist('buch[]')
           buch = Book.objects.get(id=BuchID[0])
           if BuchID[1] == '1':
              print("Rückgabe!") 
              #zurückgeben(current_user.id,BuchID[0])
              #showalert = 4
              #return HttpResponseRedirect('?title=harry%20potter&id=4#')
           else:
              #BuchID = request.POST['buch']
              buch = Book.objects.get(id=BuchID[0])         
              #print(test1)
              benutzer = User.objects.get(id=current_user.id)
              #print(test2)
              order_from_user = Order.objects.filter(users=current_user.id)
              ids    = order_from_user.values_list('books', flat=True)
              all_borrowdates_from_user = order_from_user.values_list('return_date', flat=True)
              user_has_borrowed = order_from_user.values_list('book_borrowed', flat=True)
              #print(all_borrowdates_from_user)
              if(book_over_time(all_borrowdates_from_user,current_user.id,user_has_borrowed) == False):
                 showalert = 5
              else:
                #print(list(ids))
                #print(BuchID)
                if int(BuchID[0]) in ids: #Buch wurde schon ausgeliehen
                  print(bcolors.WARNING +"WARNUNG: User: "+ str(benutzer) + " wollte Buch: "+ str(buch) + " ein weiteres mal ausleihen!" + bcolors.ENDC)
                  showalert = 2
                else: #Buch ausleihen
                  
                  if(buch.isavailable):
                   currentDate = datetime.today()
                   currentDate_timezone = timezone.make_aware(currentDate)
                   #print( "We are the {:%d, %b %Y}".format(current_date_and_time))
                   returnDate = currentDate_timezone + timedelta(days=buch.ausleihtage)
                   o = Order.objects.create(books=buch,users=benutzer,borrow_date=currentDate_timezone,return_date=returnDate,book_borrowed=False)
                   o.save()
                   showalert = 1  
                   print(bcolors.OKGREEN +"Buch ID: " + str(BuchID[0]) +" wurde von ID: " +str(current_user.id)+" ausgeliehen"+ bcolors.ENDC)
                   return HttpResponseRedirect('?title='+buch.title_small+'&id='+str(buch.id)+'&status=success')
                  else:
                   showalert = 6
                   print(bcolors.OKGREEN +"Buch ID: " + str(BuchID[0]) +" konnte nicht " +str(current_user.id)+" ausgeliehen - Kein Buch vorhanden!"+ bcolors.ENDC)
                   #weiterleitung mit success = true statt showallert
                   return HttpResponseRedirect('?title='+buch.title_small+'&id='+str(buch.id)+'&status=failed')
          orderdata = Order.objects.all()
          template = loader.get_template('products.html')
          id = request.GET['id']          
          currentbook = Book.objects.get(id=id)
          all_articels = Book.objects.all()
          context = {"currentbook": currentbook,"all_articels":all_articels,"showalert":showalert,"orderdata":orderdata}     
          return HttpResponse(template.render(context,request))

       except Exception as e:
           


           logger = logging.Logger('catch_all') # POST
           print(bcolors.FAIL +"WARNUNG: Der Ausleihprozess konnte nicht abgeschlossen werden!" +  bcolors.ENDC)
           logger.error(bcolors.FAIL +'WARNUNG: '+ str(e) + bcolors.ENDC)
           PrintException()
           showalert = 3
       try:
          orderdata = Order.objects.all()
          template = loader.get_template('products.html')
          id = request.GET['id']         
          currentbook = Book.objects.get(id=id)
          all_articels = Book.objects.all()

          context = {"currentbook": currentbook,"all_articels":all_articels,"showalert":showalert,"orderdata":orderdata}
          return HttpResponse(template.render(context,request))
       except Exception as e:
          logger = logging.Logger('catch_all')
          logger.error(bcolors.FAIL +'WARNUNG: '+ str(e) + bcolors.ENDC)
          id = 1 # 404 Book
          currentbook = Book.objects.get(id=id)
          all_articels = Book.objects.all()
          context = {"currentbook": currentbook,"all_articels":all_articels}
          print(bcolors.WARNING +"ACHTUNG: Fehler in books.views(getdetails) - Buch wurde nicht gefunden - Buch mit ID: "+ str(id) +" - "+ str(currentbook) +" wurde ausgegeben"+  bcolors.ENDC)
          return HttpResponse(template.render(context,request))

def cancelproduct(request):
    #Todo only if book isnt borrowed
    current_user = request.user
    bookID = request.GET['bookID']
    buch = Book.objects.get(id=bookID)
    zurückgeben(current_user,bookID)
    return HttpResponseRedirect('../?title='+buch.title+'&id='+bookID)

def book_over_time(borrowdates,current_user,user_has_borrowed):
    for i in range(len(borrowdates)):
       #date_time_obj = datetime.strptime(str(borrowdates[i]),'%y/%m/%d %H:%M:%S')
       currentDate = datetime.today()
       currentDate_timezone = timezone.make_aware(currentDate)
       if currentDate_timezone <= borrowdates[i]:
          print("")
       else:
          print(bcolors.WARNING+ "ACHTUNG: Abgabe wurde überschritten, Benutzer mit ID: "+ str(current_user) + " kann keine weiteren Bücher mehr ausleihen!"+ bcolors.ENDC)
          # ist das buch überhaupt abgeholt worden --> borrowed_book auf 1?
          if ( user_has_borrowed[i] == False):
            return True
          else:
            return False
    return True

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print(bcolors.WARNING + "WARNUNG: IN Zeile: " + str(lineno) + " mit Fehler: "+ bcolors.FAIL + line.strip()  + bcolors.ENDC)

def zurückgeben(UserID,BookID):
    Order.objects.filter(users=UserID,books=BookID).delete()
    print(bcolors.OKGREEN + "User: " + str(UserID) +" hat Buch mit ID: "+str(BookID)+ " zurückgegeben"  + bcolors.ENDC)
    return


def booksmainpage(request):
   print('Bücher werden angezeigt')
   try:
        genre = request.GET['genre']
        filtered_books = booksFilterwithGenre(
        request.GET,
        queryset=Book.objects.all()
        )
        all_articels = Book.objects.all()
   except:
        filtered_books = booksFilter(
        request.GET,
        queryset=Book.objects.all()
        )

        all_articels = Book.objects.all()
        #title = request.GET['title'].lower()
   finally:
        paginated_filtered_books = Paginator(filtered_books.qs, 20)
        page_number = request.GET.get('page')
        books_page_obj = paginated_filtered_books.get_page(page_number)
        context = {"filtered_books": filtered_books, "all_articels": all_articels, "books_page_obj": books_page_obj}
        #return HttpResponse(template.render(context,request))  
        return render(request,'index.html',context=context)

def indextest(request):
     print("Test wird ausgeführt")
     test1 = Book.objects.get(id=1)
     test2 = Profile.objects.get(id=12)
     o = Order.objects.create(books=test1,users=test2,borrow_date='2021-11-26 17:03:05',return_date='2021-11-26 19:03:05')
     o.save()  
     title = request.GET['title'].lower() 
     print(title)
     return 