from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product
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


@login_required
def add_to_favourite(request, product_id):
    """
    Add a product from the store to 
    favourites for the logged in user
    """
    product = get_object_or_404(Product, pk=product_id)

    favourite = Favourite.objects.get_or_create(user=request.user)
    favourite.product.add(product)



@login_required
def add_to_favourite(request, product_id):
    """
    Add a product from the store to the
    wishlist for the logged in user
    """
    product = get_object_or_404(Product, pk=product_id)

    # Create a wishlist for the user if they don't have one
    favourite, _ = Favourite.objects.get_or_create(user=request.user)
    # Add product to the wishlist
    favourite.products.add(product)
    messages.info(request, "A new product was added to your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))
