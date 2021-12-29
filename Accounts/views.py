from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Blog:blog_list')
    else:
        form = UserCreationForm()
    args = {'form': form}
    return render(request, 'Accounts/Signup.html', args)


def accounts_home(request):
    return render(request, 'Accounts/AccountsHome.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('Blog:blog_list')
    else:
        form = AuthenticationForm()
    args = {'form': form}
    return render(request, 'Accounts/Login.html', args)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'Accounts/Logout.html')

