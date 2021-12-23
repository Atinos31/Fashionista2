from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product

from django.contrib import messages
from .models import Favourite


@login_required
def favourite(request):
    """
    A view to render the user's wishlist
    """
    favourite = None
    try:
        favourite = Favourite.objects.get(user=request.user)
    except Favourite.DoesNotExist:
        pass

    context = {
        'favourite': favourite,
    }

    return render(request, 'favourite/favourite.html', context)

    def __len__(self):
        """ count all the items in the favourites"""
        return sum(item['quantity'] for item in self.favourite.values())

@login_required
def add_to_favourite(request, product_id):
    """
    Add a product from the store to the
    wishlist for the logged in user
    """
    product = get_object_or_404(Product, pk=product_id)

    # Create favourites for the user if they don't have one
    favourite, _ = Favourite.objects.get_or_create(user=request.user)
    # Add product to the favourites
    favourite.products.add(product)
    messages.info(request, 'A new product was added to your wishlist')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_favourite(request, product_id):
    """
    Add a product from the store to the
    favourite for the logged in user
    """
    favourite = Favourite.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from the favourites
    favourite.products.remove(product)
    messages.info(request, "A product was removed from your favourites")

    return redirect(request.META.get('HTTP_REFERER'))



