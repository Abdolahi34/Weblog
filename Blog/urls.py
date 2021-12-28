from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls.static import static
# from django.conf import settings


app_name = 'Blog'

urlpatterns = [
    path('', views.blog_home, name='blog_list'),
    path('<Slug>', views.article, name='article_selected')
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
