from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
#from .models import Post
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from account.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from books.models import Book
from order.models import collection
from django.contrib.auth.models import User
from order.models import Order
from datetime import datetime, date, time, timedelta
# Create your views here.

def register(request):
    if request.method == 'POST':
    # Templates of Django -> Forms
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            form.save()   
            messages.success(request, f'Konto wurde angelegt! Sie können sich nun anmelden.')
            verify_borrows(username)
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form':form})

#Ausleihtabelle zur Verifikation

# Erstellt für jeden Benutzer eine Zeile in der Tabelle Collections
# Diese wird verwendet um Daten in den QR Code zu speichern
# Pro User gibt es eine Zeile, die immer wieder aktuallisiert wird
# Somit ist immer nur 1 QR Code gültig und dieser muss immer wieder neu 
# generiert werden und es wird verhindert, dass ein 3ter eine Kopie
# des QR-Codes machen kann
def verify_borrows(user_name):
    currentuser = User.objects.get(username=user_name)
    o = collection.objects.create(user=currentuser,temp_number=0,all_orders='')
    o.save()
    return

@login_required
def profile(request):   
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): 
            u_form.save()
            p_form.save()
            messages.success(request, f'Konto wurde aktualisiert.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    # context muss in die render-Funktion als dritter Parameter übergeben werden
    return render(request, 'account/profile.html', context)

def login(request):
    return render(request, 'account/login.html')

def about(request):
    return render(request, 'account/about.html',{'title':'About'})

#schaut in tabele order und sucht alle einträge zum aktuellen user und listet sie auf -> schickt sie ins html file
@csrf_exempt
@login_required
def showmybooks(request):
    @csrf_protect
    def protected_path(request):
            print("ERROR CSRF_PROTECT IN ACCOUNT.VIEWS.PY")
    if request.method =='POST': #wenn auf einen der buttens gedrückt wurde
        if request.POST.get('isextend') == 'true' : #bedeutet es wurde der verlängern butten gedrückt

            #print(str(request.POST.getlist('idandisextend[]')[1] ))
            #order_order return date um 2 wochen verlängern
            order = __getorder__(request)
            order.return_date= order.return_date +timedelta(weeks=2)
            order.save(update_fields=['return_date']) #ohne das gehts nicht
        else: #bedeutet es wurde der stornieren butten gedrückt
            order = __getorder__(request)
            order.delete()
        return HttpResponseRedirect('#')
    else:
        # 3 Tage vorher kann man verlängern 
        current_date  = date.today() +timedelta(days=3)
        all_books = Order.objects.all()
        my_books =  all_books.filter(users_id=request.user.id)
        context = {"all_books": my_books,"current_date": current_date}
        return render(request, 'account/meinebuecher.html', context=context)


@login_required
def showmybooks2(request):
    all_books = Order.objects.all()
    my_books =  all_books.filter(users_id=request.user.id)
    context = {"all_books": my_books}
    return render(request, 'account/test2.html', context=context)

def __getorder__(request):
    bookid = int(request.POST.get('bookID'))
    allorders = Order.objects.all()
    filteredorders = allorders.filter(books_id=bookid).filter(users_id=request.user.id)
    if len(filteredorders) != 1:
        raise Exception("Größe der Liste müsste 1 sein sonst ist vielleicht ein Fehler in der Datenbank?")
    order = filteredorders[0]
    return order



