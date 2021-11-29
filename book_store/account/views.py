from django.shortcuts import render, redirect
#from .models import Post
from django.contrib import messages
from account.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from books.models import Book
from order.models import Order
# Create your views here.

def register(request):
    if request.method == 'POST':
    # Templates of Django -> Forms
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto wurde angelegt! Sie können sich nun anmelden.')
            return redirect('login-site')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form':form})

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
    #added by johannes to insert new books while runtime
    #can be deleted
    print("about to add new books")
    print(Book.objects.get(id=2))
    mybook= Book(2, 'img', 'titel', 'desc', '2021-10-10', 'author', True, 12, 'horror', 100)
    mybook.save()
    return render(request, 'account/about.html',{'title':'About'})

#schaut in tabele order und sucht alle einträge zum aktuellen user und listet sie auf -> schickt sie ins html file
def showmybooks(request):
    all_books = Order.objects.all()
    my_books =  all_books.filter(users_id=13)
    #my_books =Order.objects.get(users_id=13)
    print(my_books)
    print(all_books)
    context = {"all_books": my_books}
    # return HttpResponse(template.render(context,request))
    return render(request, 'account/test.html', context=context)
