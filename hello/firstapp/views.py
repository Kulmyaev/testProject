from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("<h2>Главная страница</h2")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponseRedirect("/about/123")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid=0):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request, id, name):  # Homework
    output = '<h2>Имя: {0}, ID: {1}</h2>'.format(name, id)
    return HttpResponse(output)


def m404(request):
    return HttpResponseNotFound('<h1>Страничка потерялась</h1>')
