from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm

'''
Accounts home page

'''
@login_required(login_url='login')
def accounts_home(request):
    return render(request, 'accounts_index.html')



def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + user)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request,'registration/register.html', {'form':form})