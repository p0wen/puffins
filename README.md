# Work in Progress

# Milestone Project 4 with *Code Institute*


# Table of Content

  * [UX](#ux)
  * [User Stories](#user-stories)
  * [Wireframes](#wireframes)
    + [Planned Layout](#planned-layout)
    + [Final Layout](#final-layout)
    + [Explanation for differences](#explanation-for-differences)
    + [Color Scheme](#color-scheme)
  * [Data Model](#data-model)
    + [Gear Collection](#gear-collection)
    + [Categories Collection](#categories-collection)
    + [Users Collection](#users-collection)
  * [Features](#features)
    + [Exisiting Features](#exisiting-features)
    + [Features Left to Implement](#features-left-to-implement)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
    + [Test Cycle](#test-cycle)
    + [Validator Checks, Audits & Tools](#validator-checks--audits---tools)
    + [Known Bugs & Issues](#known-bugs---issues)
  * [Deployment](#deployment)
    + [Local Deployment](#local-deployment)
      - [Prerequisites to work with this Site](#prerequisites-to-work-with-this-site)
      - [Step-by-Step Instructions](#step-by-step-instructions)
    + [Deployment to Heroku](#deployment-to-heroku)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)
      - [References](#references)

## UX


## User Stories

## Wireframes

### Planned Layout

#### Logo


#### Components


#### Wireframes


### Final Layout




### Explanation for differences


### Color Scheme


## Data Model
 

## Features


### Exisiting Features



### Features Left to Implement


## Technologies Used

## Testing

### Validator Checks, Audits & Tools

### Known Bugs & Issues

[ ] Update form for more than 1 item in cart

### Issues handled via development

- Templates not pulled from apps folder
-> make sure to have the following in settings.py
```
import os
DIRNAME = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'site-templates/'),
)
```

## Deployment

This site is deployed to heroku and the versioning was done with git and the Repository is hosted on Github.

### Local Deployment

#### Prerequisites to work with this Site


#### Step-by-Step Instructions



### Deployment to Heroku

## Credits

- Logo & Template for T-Shirt, Sweatshirt & Bodysuite Design created by Simone Brauner from https://www.polardots.studio/

### Content

- Written by me - inspired by twothirds.com

### Media

Category Images: 
Grown Ups: https://images.unsplash.com/photo-1490718687940-0ecadf414600?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1952&q=80
Kids: https://images.unsplash.com/photo-1490826153516-b55d176cdb9a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1952&q=80
Partnerlook: https://images.unsplash.com/photo-1528686355953-c65738cb43ea?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1242&q=80

### Acknowledgements

Special Thanks to...

... Simone from https://www.polardots.studio/
... my Code-Institute Mentor
... Tutors and Fellow Students of CI 

### References 
* read up on making drop down full width https://stackoverflow.com/questions/49659305/how-to-make-a-bootstrap-4-full-width-dropdown-in-navbar
* horzizontal line readup https://stackoverflow.com/questions/16073323/horizontal-rule-line-beneath-each-h1-heading-in-css
* tutorial on how to animate scrollbar https://www.youtube.com/watch?v=vE4UuSzR5T0
* hear animation https://designmodo.com/shopping-cart-ui/
* how to custome style navbar https://medium.com/coder-grrl/the-guide-to-customising-the-bootstrap-4-navbar-i-wish-id-had-6-months-ago-7bc6ce0e3c71
* starting point for carousel https://startbootstrap.com/snippets/full-slider/
* inspiration for a mega menu https://www.w3schools.com/howto/howto_css_mega_menu.asp
* inspiration for product names https://magoosh.com/english-speaking/english-vocab/positive-adjectives-the-ultimate-list
* bases for toggling colappsed navbar background: https://stackoverflow.com/questions/32147082/changing-collapsed-navbar-list-background-color
* how to go back to previous page https://stackoverflow.com/questions/2968425/get-back-to-previous-page
* how to style crispy forms https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#custom-fields-placement-with-crispy-forms
* how to work with ajax and django:
- https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
- https://realpython.com/django-and-ajax-form-submissions/
* how to avoid duplicates in database of productvariant (product & size) https://stackoverflow.com/questions/3052975/django-models-avoid-duplicates