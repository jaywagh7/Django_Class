from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def page1(request):
    return HttpResponse("<h1>Welcome to page 1</h1>")
def page2(request):
    return HttpResponse("<h1>Welcome to page 2</h1>")
def page3(request):
    return HttpResponse("<h1>Welcome to page 3</h1>")
def page4(request):
    return HttpResponse("<h1>Welcome to page 4</h1>")
def page5(request):
    return HttpResponse("<h1>Welcome to page 5</h1>")

