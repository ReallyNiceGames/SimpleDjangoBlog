from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    #return HttpResponse('home')
    return render(request, 'home_page.html')

def about_page(request):
    #return HttpResponse('about')
    return render(request, 'about_page.html')