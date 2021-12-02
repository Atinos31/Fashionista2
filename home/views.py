from django.shortcuts import render


# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def productPage(request):
    """ A view to return the product page """
    return render(request, 'home/product.html')
