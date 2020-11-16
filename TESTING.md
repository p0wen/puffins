# Introduction

- different testing approaches where followed
- manueal testing, user testing, automatic Tests
- furthermore code ran through validation services to spot any irregularities
- project was posted into #peer-code-review group from Code Institute to gather feedback
- interessting bugs were documented during development as a reference

# Manual Testing

## Navigation
## Footer
## Search
## Signup
## Login
## Logout
## Shop
## Highlights
## Blog
## About
## Help
## Cart
## Wishlist
## Checkout
## Useraccount
## Store-Management

# User Testing

- heroku link was shared with friends and family
- following feedback was collected
- following bugs were identified

# Automatic Tests & Continious Integration

- basic automatic tests were created to support the testing and development prodedure
- just an initial start, further tests should be written to complete 100% test coverage
- travis CI used to support continious integration with heroku and run test suite before deployment

# Validation Services
## Validation Tools
## Responsiveness & Rendering
## Browser Compatibility

# #Peer-Code-Review



# Bug-Log from Development

- following bugs were tackled during development
- updating userprofile even if checkbox is unchecked
- webhooks for orders without the optional streetaddressline2 filled out are failing. therefore customers who dont provide a line2 street adress are not receiving their order confirmation (solution: set null=true on street_address2)
- adding products to a wishlist if no item was added on a fresh user
- after editing the cart logic the checkout view broke missing / on the url
- product images not showing The {{MEDIA_URL}}image.jpg syntax is used for standalone images (i.e. that are not related to a model). But if the image is part of a model instance, then {{ item.image.url }} does the trick.
- Templates not pulled from apps folder
-> make sure to have the following in settings.py
```
import os
DIRNAME = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'site-templates/'),
)
```
- importing fixtures to postgres db led to some troubles. making sure the charfields are correct  // especially on long descriptions it makes sense to use TextField


