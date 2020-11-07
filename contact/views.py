from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from useraccount.models import UserAccount
from .models import FAQ


def contact(request):
    template = 'contact/contact.html'

    general = FAQ.objects.all().filter(category=1)
    return_policy = FAQ.objects.all().filter(category=2)
    pre_order = FAQ.objects.all().filter(category=3)
    delivery = FAQ.objects.all().filter(category=4)
    payment = FAQ.objects.all().filter(category=5)

    if request.user.is_authenticated:
        profile = UserAccount.objects.get(user=request.user)
        user_email = profile.user.email
        contact_form = ContactForm(initial={
            'first_name': profile.user.first_name,
            'last_name': profile.user.last_name,
            'email': user_email,
            })
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
        'preorder': pre_order,
        'general': general,
        'return': return_policy,
        'delivery': delivery,
        'payment': payment,
    }

    return render(request, template, context)


def contact_success(request):

    return render(request, 'contact/contact_success.html')
