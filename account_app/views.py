from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
def login_user(request):
    #اگر احراز هویت کرده بود صفحه را نبیند
    if request.user.is_authenticated == True:
        return redirect('/')
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'account_app/login.html',{"form":form})


def register_user(request):
    
    context = {"errors":[]}
     #اگر احراز هویت کرده بود صفحه را نبیند
    if request.user.is_authenticated == True:
        return redirect('/')
    
    if request.method == "POST":
         username = request.POST.get('username')
         password1 = request.POST.get('password1')
         password2 = request.POST.get('password2')
         email = request.POST.get('email')
         #اگر پسورد ها برابر نبودند
         if password1 != password2:
             context['error'].append('pass are not same!')
             return render(request, "account_app/register.html", context)
         #اگر کاربر از قبل وجود داشت
         if User.objects.get(username=username):
             context['error'].append('User is exist')
            
         
         user = User.objects.create(username=username, password=password1, email=email)
         login(request, user)
         return redirect('/')
         
    
    return render(request, "account_app/register.html")







def logout_user(request):
    logout(request)
    return redirect("/")

