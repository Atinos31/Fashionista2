from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product
from .models import WishList


@login_required
def favourite(request):
    """
    A view to render the users favourites
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    products = profile.favourite.all()
    template = 'favourite/favourite.html'
    context = {
        'products': products,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def add_to_favourite(request, product_id):
    """
    Add a product from the store to the
    wishlist for the logged in user
    """
    product = get_object_or_404(Product, pk=product_id)

    favourite = Favourite.objects.get_or_create(user=request.user)
    favourite.product.add(product)

