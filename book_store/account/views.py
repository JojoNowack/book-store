from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
#from .models import Post
from django.contrib import messages
from account.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from books.models import Book
<<<<<<< HEAD
from order.models import collection
from django.contrib.auth.models import User
=======
from order.models import Order
import datetime
>>>>>>> b151f8420994c556ab93dabda21eaf1cfc98a128
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
            return redirect('login-site')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form':form})

#Ausleihtabelle zur Verifikation


def verify_borrows(user_name):
    currentuser = User.objects.get(username=user_name)
    o = collection.objects.create(user=currentuser,temp_number=0,all_orders='')
    o.save()
    return

@login_required
def profile(request):   
    # if request.method == "POST": 
    #     p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    #     if p_form.is_valid():
    #         p_form.save()
    #         messages.success(request, f'Änderungen waren erfolgreich')
    #         return redirect('profile')
    # else:
    #     p_form = ProfileUpdateForm(instance=request.user.profile)
    # context = {
    #     'p_form' : p_form
    # } # context muss in die render-Funktion als dritter Parameter übergeben werden
    return render(request, 'account/profile.html')

def login(request):
    return render(request, 'account/login.html')

def about(request):
    return render(request, 'account/about.html',{'title':'About'})

#schaut in tabele order und sucht alle einträge zum aktuellen user und listet sie auf -> schickt sie ins html file

@login_required
def showmybooks(request):
    if request.method =='POST': #wenn auf einen der buttens gedrückt wurde
        if request.POST.getlist('idandisextend[]')[1] == 'true' : #bedeutet es wurde der verlängern butten gedrückt
            #order_order return date um 2 wochen verlängern
            order = __getorder__(request)
            order.return_date= order.return_date +datetime.timedelta(weeks=2)
            order.save(update_fields=['return_date']) #ohne das gehts nicht
        else: #bedeutet es wurde der stornieren butten gedrückt
            order = __getorder__(request)
            #quantitiy vom buch +1
            book=Book.objects.get(id=order.books.id)
            if book.quantity < 0:
                raise Exception("negative quantity ist nicht möglich")
            book.quantity= book.quantity+1
            book.save(update_fields=['quantity'])
            order.delete()
        return HttpResponseRedirect('#')
    else:
        all_books = Order.objects.all()
        my_books =  all_books.filter(users_id=request.user.id)
        context = {"all_books": my_books}
        return render(request, 'account/test.html', context=context)


def __getorder__(request):
    bookid = int(request.POST.getlist('idandisextend[]')[0])
    allorders = Order.objects.all()
    filteredorders = allorders.filter(books_id=bookid).filter(users_id=request.user.id)
    if len(filteredorders) != 1:
        raise Exception("Größe der Liste müsste 1 sein sonst ist vielleicht ein Fehler in der Datenbank?")
    order = filteredorders[0]
    return order



