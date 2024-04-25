from django.shortcuts import render

def home_page(request):
    return render(request, 'homepage.html')
def register_page(request):
    return render(request, 'register.html')