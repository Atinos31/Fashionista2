from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """ a view that renders the cart contents page"""
    return render(request, 'cart/cart.html')

