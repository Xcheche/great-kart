from django.shortcuts import render

# Create your views here.


def signup(request):
    return render(request, 'accounts/register.html')


def signin(request):
    return render(request, 'accounts/signin.html')