from django.shortcuts import render

def home_html(request):
    return render(request, "homepage.html")
