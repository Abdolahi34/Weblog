from django.shortcuts import render, Http404, HttpResponse
from . import models


def BlogHome(request):
    ArticlesObj = models.Article.objects.all().order_by('DateCreated')
    args = {'ArticlesObj': ArticlesObj}
    return render(request, 'Blog/BlogHome.html', args)

def Article(request, Slug):
    ArticleObj = models.Article.objects.all()
    CheckSlug = False
    for i in ArticleObj:
        if i.Slug == Slug:
            CheckSlug = True
            ArticleSelected = i
            break
    if CheckSlug == True:
        args = {'ArticleSelected': ArticleSelected}
        return render(request, 'Blog/Article.html', args)
    else:
        raise Http404()

