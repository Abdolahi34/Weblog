from django.shortcuts import render, Http404, HttpResponse
from . import models


def BlogHome(request):
    ArticlesObj = models.Article.objects.all().order_by('DateCreated')
    args = {'ArticlesObj': ArticlesObj}
    return render(request, 'Blog/BlogHome.html', args)

def Article(request, Slug):
    ArticleSelected = models.Article.objects.get(Slug=Slug)
    args = {'ArticleSelected': ArticleSelected}
    return render(request, 'Blog/Article.html', args)

