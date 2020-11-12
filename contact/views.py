from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm
from useraccount.models import UserAccount
from .models import FAQ


def contact(request):
    """ contact:\n
    * if it's a POST request it submits the form
     and returns json to ajax call\n
    * if it's a GET request it gets the FAQs form
     Data base & renders the contact form
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['category']
            from_email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject,
                    f"Message from: {first_name}\
                         {last_name}\n Message: \n {message}",
                    from_email,
                    [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            render_success = render_to_string('contact/contact_success.html')
            return HttpResponse(render_success, content_type="text/html")

    else:
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
