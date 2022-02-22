from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import (ListView,TemplateView,
                                    DetailView,
                                    UpdateView,
                                    DeleteView,
                                    CreateView, View)
from . import models
from .models import *
from django.conf import settings
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.



def IndexView(request):
    context={}
    return render(request,'index.html',context)    



        




        
        


