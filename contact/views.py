from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from useraccount.models import UserAccount
from .models import FAQ


def contact(request):
    template = 'contact/contact.html'

    categories = FAQ.objects.all().filter(category)
    questions = FAQ.objects.all()

    if request.user.is_authenticated:
        profile = UserAccount.objects.get(user=request.user)
        user_email = profile.user.email
        contact_form = ContactForm(initial={
            'first_name': profile.user.first_name,
            'last_name': profile.user.first_name,
            'email': user_email,
            })
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
        'categories': categories,
        'questions': questions
    }

    return render(request, template, context)


def contact_success(request):

    return render(request, 'contact/contact_success.html')
