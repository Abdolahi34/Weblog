from django.shortcuts import render

def main_page(reqquest):
    return render(reqquest, 'MainPage.html')

def about(request):
    return render(request, 'About.html')

