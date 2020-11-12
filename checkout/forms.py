#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name',
                  'last_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'zipcode', 'town_or_city', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-genereated labels
        and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-Mail Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street',
            'street_address2': 'Apartment, suite, etc.',
            'zipcode': 'Zip Code',
            'town_or_city': 'City',
            'country': 'Country',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if not self.fields[field].required:
                    placeholder = f'{placeholders[field]} (Optional)'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
