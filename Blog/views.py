from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms


def blog_home(request):
    articles_obj = models.Article.objects.all().order_by('date_created')
    args = {'articles_obj': articles_obj}
    return render(request, 'Blog/BlogHome.html', args)


def article(request, slug):
    article_selected = models.Article.objects.get(slug=slug)
    args = {'article_selected': article_selected}
    return render(request, 'Blog/Article.html', args)


@login_required(login_url='Accounts:login')
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save
            return redirect('Blog:blog_list')
    else:
        form = forms.CreateArticle()
    args = {'form': form}
    return render(request, 'Blog/CreateArticle.html', args)

