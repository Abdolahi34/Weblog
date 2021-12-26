from django.shortcuts import render, Http404, HttpResponse
from . import models


def BlogHome(request):
    ArticlesObj = models.Article.objects.all().order_by('DateCreated')
    args = {'ArticlesObj': ArticlesObj}
    return render(request, 'Blog/BlogHome.html', args)

def Article(request, Slug):
    ArticleObj = models.Article.objects.all()
    CheckSlug = False
    for ArticleOne in ArticleObj:
        if ArticleOne.Slug == Slug:
            CheckSlug = True
            break
    if CheckSlug == True:
        args = {'ArticleObj': ArticleObj}
        return render(request, 'Blog/Article.html', args)
    else:
        return HttpResponse('fvfvfvf')

