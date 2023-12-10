from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("<h2>Главная страница</h2>")  # HttpResponse


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


# def contact(request):
#   return HttpResponseRedirect("<h2>Контакты</h2>")

def contact(request):
    return HttpResponseRedirect("/about/123")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid=0):  # productid=0
    category = request.GET.get("cat", "")
    output = "<h2>Продукт Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request, id=0, name="Undefined"):# дз по умолчанию
    output = '<h2>{0}, ID: {1}</h2>'.format(id, name)
    return HttpResponse(output)


def m404(request):
    return HttpResponseNotFound('<h1>Страничка потерялась</h1>')
