from django.shortcuts import render, get_object_or_404

from .models import UserProfile

# Create your views here.
def profile(request):
    """
    display the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
