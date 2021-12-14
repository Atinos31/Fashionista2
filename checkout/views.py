from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_keys': 'pk_test_51JhYupGH6l0eIhtu7sPNZz7G0Tl6WJtrWvNlyyjLRvpjsU8irW3hvymwxSWjALD2YZzIVMqw4zrAy2oPjzevru4S00iirNh65v',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
