from django.shortcuts import render, redirect
#from .models import Post
from django.contrib import messages
from account.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from books.models import Book
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
    return render(request, 'account/about.html',{'title':'About'})


def test(request):
    context = {}
    all_articels = Book.objects.all()

    context = {"all_articels": all_articels}
    #return HttpResponse(template.render(context,request))
    return render(request,'account/test.html',context=context)

