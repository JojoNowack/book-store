from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from account.forms import UserRegisterForm
# Create your views here.

# def loginView(request):
#     return render(request, "login.html",{})

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
    
    
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'account/login.html', context)

def about(request):
    return render(request, 'account/about.html',{'title':'About'})