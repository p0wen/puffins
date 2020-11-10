# Work in Progress

# Milestone Project 4 with *Code Institute*

![Puffins](https://thepuffins.s3.eu-central-1.amazonaws.com/github-docs/puffins_amiresponsive.gif)

_"Always be yourself. Unless you can be a puffin, then always be a puffin."_

We at [__puffins__](https://thepuffins.herokuapp.com) are dedicated to provide beautiful, uniting and sustainable products to individuals, love birds and families. With our mehtod to only produce whats demanded by our customers and delivering longlasting, high quality products we want to counter the biggest problems of the western society. Our products are locally produced in Europe and we only use materials where we know the origin, to guarantee 100% ethical and sustainable products.

This site is the final Milestone Projects that made up the Full Stack Web Development Course at Code Institute. The core requirements focus on bulding a fullstack site with the use of Django, Python, JavaScript, HTML, CSS and a relational database. The final result is hosted on Heroku, while storing static and media files on an S3 Cloudstorage from AWS. The store is connected to [Stripe](www.stripe.com).

To test the site incl. the checkout process please use the test credit card number provided in the [Stripe Documentation](https://stripe.com/docs/testing):

+ __Number__: 4242 4242 4242 424 4242
+ __Exp. Date__: Anything (e.g. 02/24)
+ __CVC__: Anything (e.g. 007)

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

# UX

## Purpose and Aim of the Project

The aim of this project is to create an ecommerce shop for sustainable clothing especially targeted towards young couples and families. The goal is to create this shop as an interactive fullstack website that allows customers to browse products, make purchases by credit card and if registered manage a wishlist or see their orderhistory. These goals should be supported by providing a clean and easy to use website that allows seamless navigation and has a low bounce rate.

## Design process
Before laying out the project and creating an initial design market research was done. During this research phase the following questions were also acknowledged: 
* How do other stores look?
* What are typical design patterns used across stores?
* Which site are appealing to me?
* Which kind of stores fit to my business idea? 

The final layout was influenced by the following sites:
* [twothirds.com](https://twothirds.com/)
* [taylorstich.com](https://www.taylorstitch.com/)
* [manitober.de](https://www.manitober.de/)

## Target group

* women and men aged between 25 and 40 years 
* who care about the environment,
* especially coupls who may have 1 or 2 children in the age of 6 month to 12 years
* mid-high income
* with a passion for living outdoors and owning sustainable high quality products

## Epics & User Stories
Before the start of the Project the Epics and User Stories were defined and written out to have complete set of necessary features to get the site going. In total 6 Epics were defined and user stories were broken down into 3 user groups: regular site visitors, registered site visitors and the store manager/owner.

### EPIC: Browse Site
As a __site visitor__, i want to...
* ... __access the website__ with any device (smartphone, tablet, desktop), so that i am able to visit the shop anytime and anywhere.
* ... have __easy navigation__, to quickly solve the reason for my visit.
* ... have __information about the brand__, to get to know the company and understand their mission and story.
* ... be able to __contact the company__, so that i quickly can get in touch if i have a question or issue.

### Epic: Browse Products
As a __site visitor__, i want to...
* ... browse products by __category and productline__, so that i quickly find what i am looking for.
* ... __sort products__, to adjust the order according to my needs.
* ... be able to __search for specific products__, to quickly get what i need.
* ... to __access product details__, to get more information on an item.
* ... be able to __choose a size__, to order the necessary items according to my needs.

### Epic: Manage Cart & Make Purchase
As a __site visitor__, i want to...
* ... see all my __items in a cart__, so that i have an overview of my potential purchase.
* ... be able to __reduce / increase quantity__, so that i can order my prefered amount.
* ... be able to __remove an item from my cart__, so that i can manage my cart efficiently.
* ... be able to __checkout from the cart__ view, so that i can quickly finish my purchase.
* ... be able to __pay a order by credit card__, so that i don't have to deal with an invoice and money transfer.
* ... __receive an order confirmation__, so that i know my order was received.

As a __registered user__, i want to...
* ... have my __details prefilled from my profile__, so that i quickly can finish my purchase

### Epic: Registration & Useraccount

As a __site visitor__, i want to...
* ... be able to __sign up to the store__, so that i can track orders and have my data prefilled in the order form.

As a __registered user__, i want to...
* ... be __able to login__, so that i can access my useraccount.
* ... be able to __see my order history__, so that i know what i've purchased in the past.
* ... __manage my personal details__, so that i can quickly update my data if something changes.

### Epic: Manage Wishlist
As a __registered user__, i want to...
* ... __add/remove items to my wishlist__, so that can save items for later purchase to my useraccount.
* ... have an __overview of my wishlist__, to get an overview of my already added products.

### Epic: Store Management
As a __store owner__, i want to...
* ... be able to __manage the products, categories, productlines and productvariants__, so that i have an overview of my inventory.
* ... __manage blog entries__, to add new/edit posts on the blog to provide customers some additional value.
* ... __manage FAQs__, so that i can quickly update often asked questions

## Layout, Styling & Wireframes

The wireframes were created in Figma. Figma is a cloud based desing tool which allows you to rapidly create prototypes, wireframes and layouts [Figma](www.figma.com)

The whole figma project can be accessed here:
[Puffins - Wireframes](https://www.figma.com/file/MhxXXrKoRhGyWMhX1cug2U/puffins?node-id=0%3A1)

#### Logo

The puffins logo was created by [polardots](https://www.polardots.studio/). It shows a vector style puffin stand upright and is signaling joy to the world!

![Puffins Logo](https://thepuffins.s3.amazonaws.com/media/puffin_icon.png)

The puffins text logo was created by me with [Figma](www.figma.com).

![Puffins Textlogo](https://thepuffins.s3.amazonaws.com/media/puffins_logo_dark.svg)

#### Color Scheme

The color scheme was chosen with the goal to represent a lightweight modern website. The colors are taken from the base colors of the puffin bird.

![Color Scheme](https://thepuffins.s3.eu-central-1.amazonaws.com/github-docs/puffins_colorscheme.png)

#### Components

Components were created in [Figma](www.figma.com):

![Puffins - Components](https://thepuffins.s3.eu-central-1.amazonaws.com/github-docs/puffins_components.png)

#### Wireframes

The whole figma project can be accessed here:
[Puffins - Wireframes](https://www.figma.com/file/MhxXXrKoRhGyWMhX1cug2U/puffins?node-id=0%3A1)

Mobile:

![Puffins - Mobile](https://thepuffins.s3.eu-central-1.amazonaws.com/github-docs/puffins_mobile.png)

Medium - width screen:

![Puffins - Mobile](https://thepuffins.s3.eu-central-1.amazonaws.com/github-docs/puffins_medium.png)

Desktop - large screen:
![Puffins - Mobile](https://thepuffins.s3.eu-central-1.amazonaws.com/github-docs/puffins_large.png)

### Final Layout

--> INSERT AM I RESPONSVIE SCREENSHOT

### Explanation for differences



## Database structure

During development the built-in SQLite3 database from django is used. However, for the deployment to Heroku a switch to postgressql was undertaken.
[Django’s authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/) in combination with [django-allauth](https://django-allauth.readthedocs.io/en/latest/overview.html) is used to manage users and permissions.
The structure of the products and checkout app are based on the [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) project from Code Institute.

### Categories

| Name         | Type       | Example Data                                                 |
|--------------|------------|--------------------------------------------------------------|
| name         | CharField(max_length=254)  | grown_ups                                                    |
| display_text | CharField(max_length=254)  | Grown Ups                                                    |
| image        | ImageField(null=True, blank=True) | grownup_puffin.png                                           |
| image_url    | URLField(max_length=1024, null=True, blank=True)   | https://thepuffins.s3.amazonaws.com/media/grownup_puffin.png |

### Productline

| Name         | Type      | Example Data |
|--------------|-----------|--------------|
| name         | CharField(max_length=50) | tshirt       |
| display_text | CharField(max_length=254) | T-Shirt      |

### Products
| Name                | Type                                                                                           | Example Data    |
|---------------------|------------------------------------------------------------------------------------------------|-----------------|
| category            | ForeignKey( 'Category')                                                                        | 1               |
| productline         | ForeignKey( 'ProductLine')                                                                     | 1               |
| name                | CharField( max_length = 254 )                                                                  | passionate      |
| display_text        | CharField( max_length = 254 )                                                                  | Passionate Puffin |
| price               | DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True) | 49.95     |
| discount_price      | DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True) | 39,96     |
| is_on_sale          | BooleanField(default=False)                                                                    | True      |
| avail_for_pre_order | BooleanField( default = False )                                                                | False     |
| date_of_dispatch    | CharField( max_length = 254 ,  blank = True ,  null = True )                                   | null      |
| discontinued        | BooleanField( default = False )                                                                | false     |
| image               | ImageField( null = True ,  blank = True )                                                      | passionatepuffin.png |
| image_url           | URLField( max_length = 1024 ,  null = True ,  blank = True )                                   | https://thepuffins.s3.amazonaws.com/media/passionatepuffin.png  |
| description         | TextField( null = True ,  blank = True )                                                       | Made with love and passion: the passionate puffin with its super soft, lightweight cotton fabric and neps in contrast colour has the perfect fit. Wear it on its own or as a base layer under a cardigan. Made the Puffins way, from organic linen from the EU for a great sustainable tee. T-shirts made from linen make you stay cool in the summer . They are more durable and also feel lighter. |
| is_featured         | BooleanField( default = False ,  null = True ,  blank = True )                                 | True        |
| color               | CharField( max_length = 254 ,  null = True )                                                   | grey        |
| material_1          | CharField( max_length = 254 ,  null = True ,  blank = True )                                   | linen       |
| material_2          | CharField( max_length = 254 ,  null = True ,  blank = True )                                   | ""          |

### Productsize

| Name         | Type                                                | Example                                                                                                          |
|--------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| SIZE_CHOICES |                                                     | [('NO', 'None'), ('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'),] |
| shirt_size   | CharField( max_length = 2 ,  choices =SIZE_CHOICES) | XS                                                                                                               |

### Productvariant

| Name     | Type                                                  | Example |
|----------|-------------------------------------------------------|---------|
| product  | ForeignKey('Product', on_delete=models.CASCADE)       | 1       |
| size     | ForeignKey('ProductSize', on_delete=models.CASCADE)   | XS      |
| quantity | IntegerField( validators =[MinValueValidator( 0.0 )]) | 9       |

### Order

| Name              | Type           |
|-------------------|----------------|
| order_number      | CharField( max_length = 32 ,  null = False ,  editable = False )    |
| user_profile      | ForeignKey(UserAccount,  on_delete =models.SET_NULL,null = True ,  blank = True ,related_name = 'orders' ) |
| order_status      | CharField( max_length = 1 ,  choices =STATUS_OPTIONS,                                      default = '0' )  |
| first_name        | CharField( max_length = 50 ,  null = False ,  blank = False )                                                |
| last_name         | CharField( max_length = 50 ,  null = False ,  blank = False )                                                |
| email             | EmailField( max_length = 254 ,  null = False ,  blank = False )                                              |
| phone_number      | CharField( max_length = 20 ,  blank = True )                                                                 |
| country           | CountryField( blank_label = 'Country' ,  null = False ,  blank = False )                                     |
| zipcode           | CharField( max_length = 20 ,  null = True ,  blank = False )                                                 |
| town_or_city      | CharField( max_length = 40 ,  null = False ,  blank = False )                                                |
| street_address1   | CharField( max_length = 80 ,  null = False ,  blank = False )                                                |
| street_address2   | CharField( max_length = 80 ,  blank = True )                                                                 |
| total_order       | DecimalField( max_digits = 10 ,  decimal_places = 2 ,  null = False ,  default = 0 )                         |
| total_tax         | DecimalField( max_digits = 10 ,  decimal_places = 2 ,  null = False ,  default = 0 )                         |
| tax_rate          | DecimalField( max_digits = 6 ,  decimal_places = 2 ,  null = False ,  default = 0 )                          |
| delivery_cost     | DecimalField( max_digits = 10 ,  decimal_places = 2 ,  null = False ,  default = 0 )                         |
| grand_total       | DecimalField( max_digits = 10 ,  decimal_places = 2 ,  null = False ,  default = 0 )                         |
| date_order_placed | DateTimeField( auto_now_add = True )                                                                         |
| original_cart     | TextField( null = False ,  blank = False ,  default = '' )                                                   |
| stripe_pid        | CharField( max_length = 254 ,  null = False ,  blank = False ,  default = '' )                               |

### OrderLineItem

| Name           | Type                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------|
| order          | ForeignKey(Order,  null = False ,  blank = False ,  on_delete =models.CASCADE,  related_name = "lineitems" ) |
| productvariant | ForeignKey(ProductVariant,  null = False ,  blank = False ,  on_delete =models.CASCADE)                      |
| quantity       | IntegerField( blank = False ,  default = 0 )                                                                 |
| lineitem_total | DecimalField( max_digits = 6 ,  decimal_places = 2 ,  null = False ,  default = 0 ,  editable = False )      |

### Useraccount

| Name                    | Type                                                                   |
|-------------------------|------------------------------------------------------------------------|
| user                    | OneToOneField(User,  on_delete =models.CASCADE)                        |
| default_phone_number    | CharField( max_length = 20 ,  null = True ,  blank = True )            |
| default_street_address1 | CharField( max_length = 80 ,  null = True ,  blank = True )            |
| default_street_address2 | CharField( max_length = 80 ,  null = True ,  blank = True )            |
| default_zipcode         | CharField( max_length = 20 ,  null = True ,  blank = True )            |
| default_town_or_city    | CharField( max_length = 40 ,  null = True ,  blank = True )            |
| default_country         | CountryField( blank_label = 'Country' ,  null = True ,  blank = True ) |

### Wishlist

| Name            | Type                                                                                    |
|-----------------|-----------------------------------------------------------------------------------------|
| user_profile    | OneToOneField(UserAccount,  on_delete =models.CASCADE, null = False ,  blank = False)   |
| wished_products | ManyToManyField(Product, related_name = 'userwishlists' )                               |

### FAQs

| Name             | Type                                                                                                              |
|------------------|-------------------------------------------------------------------------------------------------------------------|
| CATEGORY_CHOICES | [( '1' ,  'General' ), ( '2' ,  'Return' ), ( '3' ,  'Pre Order' ), ( '4' ,  'Delivery' ), ( '5' ,  'Payment' ),] |
| category         | CharField( max_length = 1 ,  choices =CATEGORY_CHOICES)                                                           |
| name             | CharField(max_length = 120 , null = True, blank = False )                                                         |
| title            | CharField(max_length = 120 ,  null = True ,  blank = False )                                                      |
| answer           | TextField()                                                                                                       |
| created_at       | DateTimeField(auto_now_add = True ,null = False )                                                                 |
| updated_at       | DateTimeField(auto_now = True ,  null = False)                                                                    |
### Blog 

| Name                | Type                                                                                |
|---------------------|-------------------------------------------------------------------------------------|
| author              | ForeignKey(UserAccount,  on_delete =models.CASCADE,  null = False ,  blank = True ) |
| title               | CharField(max_length=120, null=True, blank=False)                                   |
| subtitle            | CharField(max_length=180, null=True, blank=False)                                   |
| body                | TextField()                                                                         |
| slug                | SlugField(unique=True, max_length=250, default=None)                                |
| created_at          | DateTimeField(auto_now_add=True, null=False)                                        |
| updated_at          | DateTimeField(auto_now=True, null=False)                                            |
| title_image         | ImageField(null=True, blank=True)                                                   |
| title_image_url_1   | URLField(max_length=1024, null=True, blank=True)                                    |
| content_image_1     | ImageField(null=True, blank=True)                                                   |
| content_image_url_1 | URLField(max_length=1024, null=True, blank=True)                                    |
| content_image_2     | ImageField(null=True, blank=True)                                                   |
| content_image_url_2 | URLField(max_length=1024, null=True, blank=True)                                    |

## Features



:toolbox: = Future Development

:white_check_mark: = Implemented

:x: = Feature removed

## Technologies Used
* Django
* Python
* HTML5
* CSS3
* JavaScript
* jQuery
* Bootstrap 4.5.2
* Gitpod
* Git Version Control
* GitHub
* Heroku
* S3 Cloudstorage from AWS 

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

### Content & Products

- Written by me - inspired by twothirds.com
- All Products have been created by myself with Figma

### Media

Category Images: 
* Grown Ups: https://images.unsplash.com/photo-1490718687940-0ecadf414600?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1952&q=80
* Kids: https://images.unsplash.com/photo-1490826153516-b55d176cdb9a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1952&q=80
* Partnerlook: https://images.unsplash.com/photo-1528686355953-c65738cb43ea?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1242&q=80

### Acknowledgements

Special Thanks to...

* ... https://www.polardots.studio/
* ... my Code-Institute Mentor
* ... Tutors and Fellow Students of CI 

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
* database tables in markdown created with: https://www.tablesgenerator.com/markdown_tables