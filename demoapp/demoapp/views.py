from django.shortcuts import render
from django.http import JsonResponse
from .user_list import users

def home_page(request):
    return render(request, 'homepage.html')
def register_page(request):
    return render(request, 'register.html')
def get_data(request):
    # Your logic to retrieve data
    data = {
        "username": users[0].username,
        "email": users[0].email
    }
    return JsonResponse(data)