from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
from django.shortcuts import render

from blog.models import *


def index(request):
    posts = Post.objects.all().order_by("-time_create")

    return render(request, 'blog/index.html', {'title': 'Главная', 'posts': posts})


def categories(request, article):
    return HttpResponse(f"<h1>Новости по категориям</h1><p>{article}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Стараница не найдена</h1>')
