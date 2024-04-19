from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<div style='background-color: black'><span style='color: white'>Hi, Hello</span></div>")

def admin(request):
    return HttpResponse("This is Admin Page")

def test(request):
    return HttpResponse("test")