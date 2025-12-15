from django.shortcuts import render, redirect
from .models import *
from .forms import *

def base(request):
    return render(request, "base.html")