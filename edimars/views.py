from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . forms import CreateUserForm, LoginForm, ContactForm
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.conf import settings


@login_required(login_url='login')
def homepage(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    
    form = ContactForm()
    
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile_phone = form.cleaned_data['mobile_phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            html = render_to_string('core/emails/contactform.html', {
                'name': name,
                'email': email,
               'mobile_phone': mobile_phone,
               'subject': subject,
               'message': message
            })
            
            # print('the message is successfully submitted!')
            
            send_mail('the contact form subject', 'this is the message', 'noreply@codewithedimars.com', ['cemus24@gmail.com'], html_message=html, fail_silently=False)
            
            return redirect('homepage')
    else:
        form = ContactForm()
                
    return render(request, 'core/contact.html', {
        'form': form
    })


def sendanemail(request):
    if request.method == 'POST':
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        #print(to, content)
        send_mail(
            #subject
            'From Edi_Mrs for ...',
            #message
            content,
            #from email
            settings.EMAIL_HOST_USER,
            #to email
            [to],
            #html message
            #fail_silently=False
        )
        
        return render(
            request,
            'core/email.html',
            {'title': 'send an email'}
        ) 
        
    else:
        return render (
            request, 'core/email.html',
            {'title': 'send an email'}
        )  
             

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
                
                return redirect("main")
            
    context = {'loginform': form}        
        
    return render(request, 'core/login.html', context=context)


def main(request):
    return render(request, 'core/main.html')


def client(request):
    #this client form will be redirected to payment form. After payment it will be redirected to homepage.
    return render(request, 'core/client.html')


def member(request):
    # this membership form can only be redirected to payment form. After payment it will be redirected to dashboard
    return render(request, 'core/member.html')


# @login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


def forgotPassword(request):
    return render(request, 'core/forgot-password.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def blog(request):
    return render(request, 'core/blog.html')



