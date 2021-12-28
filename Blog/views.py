from django.shortcuts import render, Http404
from . import models


def blog_home(request):
    articles_obj = models.article.objects.all().order_by('date_created')
    args = {'articles_obj': articles_obj}
    return render(request, 'Blog/BlogHome.html', args)


def article(request, Slug):
    article_selected = models.article.objects.get(Slug=Slug)
    args = {'article_selected': article_selected}
    return render(request, 'Blog/Article.html', args)


def create_article(request):
    return render(request, 'Blog/CreateArticle.html')

