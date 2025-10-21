from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Homepage!")

def some_view(request):
    if request.method == "POST":
        # your code here
        pass
