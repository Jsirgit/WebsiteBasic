from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
from .models import Post
# # Create your views here.
# #def home(request):
#  #   return HttpResponse('<h1> Blog Home </h1>')
def home(request):
     return render(request,'home.html')

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')

def service(request):
     return render(request,'service.html')

