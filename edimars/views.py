from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    return render(request, 'core/index.html')


def edit(request):
    pass


def delete(request):
    pass


def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('login')
        
    context = {'registerform': form}    
        
    return render(request, 'core/register.html', context=context)


def login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect("dashboard")
            
    context = {'loginform': form}        
        
    return render(request, 'core/login.html', context=context)

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


def logout(request):
    pass
