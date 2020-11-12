from django import forms


class ContactForm(forms.Form):
    """
    A contact form for customers
    """

    CATEGORY_CHOICES = [
        ('1', 'General'),
        ('2', 'Return'),
        ('3', 'Pre Order'),
        ('4', 'Delivery'),
        ('5', 'Payment'),
    ]
    first_name = forms.CharField(label="", max_length=30,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=30,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Last Name'}))
    email = forms.EmailField(label="", max_length=254,
                             widget=forms.TextInput(attrs={
                                  'placeholder': 'E-Mail'}))
    category = forms.CharField(
        label="", widget=forms.Select(choices=CATEGORY_CHOICES))
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Your Message', "rows": 10, }))

    class Meta:
        fields = ['first_name', 'last_name', 'email', 'category', 'message']
