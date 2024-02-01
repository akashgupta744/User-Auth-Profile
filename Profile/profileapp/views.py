from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.

def base_page(request):
    return render(request,'base.html' )


def register_page(request):
    UFO = UserForm()
    PFO = ProfileForm()
    d = {'UFO':UFO, 'PFO':PFO}

    if request.method == 'POST':
        UFD = UserForm(request.POST)
        PFD = ProfileForm(request.POST)
        print(request.POST)

        if UFD.is_valid() and PFD.is_valid():
            MUFDO = UFD.save(commit = False)
            pw1=UFD.cleaned_data['password1']
            pw2=UFD.cleaned_data['password2']
            MUFDO.set_password(pw1)
            MUFDO.set_password(pw2)
            MUFDO.save()

            MPFDO = PFD.save(commit = False)
            MPFDO.user = MUFDO
            MPFDO.save()
            send_mail('register',
            ' Thank you, your Registration is successfull',
            'akgupta7440@gmail.com',
            [MUFDO.email],
            fail_silently=False,
            )
            messages.info(request,'Account is Created')
            return HttpResponseRedirect(reverse('login_page'))
        
        else:
            d = {'UFO':UFO, 'PFO':PFO}
            messages.info(request, 'Invalid Credentials')
            # return render(request, 'register_page.html', d)
            
    return render(request, 'register_page.html',d)


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        AUO = authenticate(username=username, password=password)
        
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            messages.info(request, f'{username}, you are logged in.')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.info(request, 'Invalid username or password')
            # return redirect('login')

    return render(request,'login_page.html')

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')