from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from.forms import RegisterForm
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .models import Users
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import login as login_auth
from django.urls import reverse
from .decorators import not_authenticated


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        registerForm = RegisterForm
        return render(request, 'register.html', {'registerForm': registerForm})
    
    elif request.method == "POST":
        registerForm = RegisterForm(request.POST)
        
        if registerForm.is_valid():
            form_new = registerForm.save(commit=False)
            form_new.is_active = False
            form_new.save()
            return redirect(reverse('login'))
        
        else:
             return render(request, 'register.html', {'registerForm': registerForm})
         
def active_account(request, uidb4, token):
    User = get_user_model()
    uid = force_str(urlsafe_base64_decode(uidb4))
    user = User.objects.filter(pk=uid)
    
    if (user := user.first()) and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login_auth(request, user)
        messages.add_message(request, constants.SUCCESS, 'User active successfully')
        return redirect(reverse('login'))
    
    else:
        messages.add_message(request, constants.ERROR, 'Url inválid')
        return redirect(reverse('login'))
    
@not_authenticated
def login(request):
    return render(request, 'login.html')  
