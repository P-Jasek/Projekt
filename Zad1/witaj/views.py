from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Witaj w Django!")

def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})