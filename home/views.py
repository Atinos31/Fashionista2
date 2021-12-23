from django.shortcuts import render


# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about(request):
    """ a view to render about page"""
    return render(request, 'home/about.html')
