from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def hello(request):
#     my_list = [1,2,3,4 "String"]
#     return HttpResponse(my_list)

def hello(request):
    body = """ 
    <h1>Привет</h1>
    <p>Параграф</p>
    """
    return HttpResponse(body)

def index(request):
    context = {
        "title": "Главная страница",
        "my_list": [1,2,3,4,5],
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "title": "О нас"
    }
    return render(request, "about.html", context)

def contact(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "contacts.html", context)

