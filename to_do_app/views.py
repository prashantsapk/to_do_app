
from django.shortcuts import render,redirect

# Create your views here.

def redirecttohome(request):
    return redirect('homepage')

