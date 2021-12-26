from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

def SignUp(request):
    Forms = UserCreationForm()
    args = {'Forms': Forms}
    return render(request, 'Accounts/SignUp.html', args)
