from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Accounts'

urlpatterns = [
    path('', views.accounts_home, name='accounts_home'),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()

