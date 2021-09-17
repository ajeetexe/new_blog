from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, "blog/index.html")


def register_request(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successfull...")
            return redirect("home")
        messages.error(request, "Unsuccessfull registration, please try again...")
    form = RegistrationForm()
    return render(request, "auth/register_form.html", context={"register_form": form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'you logged in as {username}')
                return redirect('home')
            else:
                messages.error(request,'Username and password are incorrect')
        else:
            messages.error(request,'Username and password are incorrect')
    form = AuthenticationForm()
    return render(request=request,template_name='auth/login_form.html',context={'login_form':form})


def logout_request(request):
    logout(request)
    return redirect('home')