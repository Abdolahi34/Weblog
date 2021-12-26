from django.shortcuts import HttpResponse, render

def MainPage(reqquest):
    return render(reqquest, 'MainPage.html')

def About(request):
    return render(request, 'About.html')

