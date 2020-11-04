from django.shortcuts import render, get_object_or_404

from .models import UserAccount


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserAccount, user=request.user)

    template = 'useraccount/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)