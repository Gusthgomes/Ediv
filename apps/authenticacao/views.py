from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from.forms import RegisterForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        registerForm = RegisterForm
        return render(request, 'register.html', {'registerForm': registerForm})
    
    elif request.method == "POST":
        registerForm = RegisterForm(request.POST)
        
        if registerForm.is_valid():
            registerForm.save()
            return HttpResponse("Salvo com sucesso!")
        
        else:
             return render(request, 'register.html', {'registerForm': registerForm})
        
