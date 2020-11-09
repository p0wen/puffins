# Work in Progress

# Milestone Project 4 with *Code Institute*

---> INSERT AM I RESPONSIVE GIF

_"Always be yourself. Unless you can be a puffin, then always be a puffin."_

We at [__puffins__](https://thepuffins.herokuapp.com) are dedicated to provide beautiful, uniting and sustainable products to individuals, love birds and families. With our mehtod to only produce whats demanded by our customers and delivering longlasting, high quality products we want to counter the biggest problems of the western society. Our products are locally produced in Europe and we only use materials where we know the origin, to guarantee 100% ethical and sustainable products.

This site is the final Milestone Projects that made up the Full Stack Web Development Course at Code Institute. The core requirements focus on bulding a fullstack site with the use of Django, Python, JavaScript, HTML, CSS and a relational database. The final result is hosted on Heroku, while storing static and media files on an S3 Cloudstorage from AWS. The store is connected to [Stripe](www.stripe.com).

To test the site incl. the checkout process please use the test credit card number provided in the [Stripe Documentation](https://stripe.com/docs/testing):

+ Number: 4242 4242 4242 424 4242
+ Exp. Date: Anything (e.g. 02/24)
+ CVC: Anything (e.g. 007)

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

- ecommerce shop for sustainable clothing especially for families
-  

## User Stories

### Epic: Browse Products
### Epic: Make Purchase
### Epic: Registration & Useraccount
### Epic: Manage Wishlist
### Epic: Manage Store

## Layout, Styling & Wireframes

The wireframes were created in Figma. Figma is a cloud based desing tool which allows you to rapidly create prototypes, wireframes and layouts (www.figma.com)

#### Logo

vector base Logo
showing a puffin
brand text logo created in figma
google fonts used for

#### Components

-->INSERT SCREENSHOT OF COMPONENTS


#### Wireframes

--> INSERT SCREENSHOT / LINK TO FIGMA FILE

### Final Layout

--> INSERT AM I RESPONSVIE SCREENSHOT

### Explanation for differences



### Color Scheme

The color scheme was chosen with the goal to represent a lightweight modern website. The colors are taken from the base colors of the puffin bird.

--> INSERT COLORSCHEME:

--> LIST COLOR CODES:

## Data Model

--> INSERT DATABASE MODEL FOR PRODUCTS

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

- Logocreated by https://www.polardots.studio/

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
* how to handle names https://stackoverflow.com/questions/12340789/split-first-name-and-last-name-using-javascript
* how to control dates in template: https://ourcodeworld.com/articles/read/555/how-to-format-datetime-objects-in-the-view-and-template-in-django
* work with many to many fields https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/
* how to build your own blog https://medium.com/swlh/building-your-own-django-blog-part-2-78adbc516992