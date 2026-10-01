from django.shortcuts import render

def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})