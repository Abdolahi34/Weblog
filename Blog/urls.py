from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Blog'

urlpatterns = [
    path('', views.BlogHome, name='BlogHome'),
    path('<Slug>', views.Article, name='Article')
]

urlpatterns += staticfiles_urlpatterns()