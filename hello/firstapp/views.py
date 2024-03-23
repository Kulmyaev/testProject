from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h2>Главная страница</h2")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def products(request, productid):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def user(request, id, name):
    output = '<h2>Имя: {0}, ID: {1}</h2>'.format(name, id)
    return HttpResponse(output)