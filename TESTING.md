# Introduction

- different testing approaches where followed
- manueal testing, user testing, automatic Tests
- furthermore code ran through validation services to spot any irregularities
- project was posted into #peer-code-review group from Code Institute to gather feedback
- interessting bugs were documented during development as a reference

# Manual Test Cycles

## 1. Test Navbar

### General Functionalities

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click every nav item

### Logged in and non-logged in users see different options

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Check if navbar contains  
   Shop  
   Highlights  
   Blog  
   About  
   Help  
   Userprofile-icon  
   Cart-icon  
   Search-icon  
4. Click Userprofile-icon and sign in
5. Check that navbar icons changed and the follow are present  
   Useraccount-icon  
   Wishlist-icon  
   Cart-icon  
   Search-icon  

### Searchbar opens below nav when search icon is clicked

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Search-icon
5. Searchbar should open below nav

### Fixed to top and transparent :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Don't scroll check that nav is transparent

### Changes background and font color on scroll 

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Scroll and check that nav background changes to white and font to black

### Changes background and font color if collapsed on small screens

1. Open Browser on medium screen
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Don't scroll
4. Click collapse button
5. Check that nav background changes to white and font to black

## 2. Footer

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Scroll to bottom
4. Check that  
   Logo is displayed  
   Quicklinks to products are available  
   Contact details are accessabile 
   Link to About page is present

## 3. Landing Page

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Check that  
   Caroussel with images is behind nav  
   Check that no more than 4 random Products are displayed  
   Product details can be accessed by clicking the SHOP Button 

## 4. About Page

### About Page through Navbar
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on About in Navigation
4. Check that ...  
   Vision is diplayed  
   Short introduction to company is provided

### About Page through Navbar
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Scroll to bottom of page
3. Click on About in Footer
4. Check that same information is present as in Test 4.1

## Help / Contact Page
* FAQ are diplayed :white_check_mark:
* FAQs are categorized :white_check_mark:
* Contact form available for User :white_check_mark:
* Chat Option to provide direct support :toolbox:

## Shop
* Products can be browsed by Category (e.g. Kids) :white_check_mark:
* Products can be browsed by Category & Productline (e.g. Kids -> T-Shirt) :white_check_mark:
* Products can be sorted by...  
   ...Featured Products :white_check_mark:  
   ...Price :white_check_mark:
   ...Color :white_check_mark:  
   ...Name :white_check_mark:  
* Products have different labels based on  
   Normal Product :white_check_mark:  
   Sale Product :white_check_mark:  
   Pre-Order Productn:white_check_mark:  
* Product Details have a Select Option if different sizes are available :white_check_mark:
* Product Details have only a "Add to Cart" button if unisize item :white_check_mark:
* Product can be shared on social media :toolbox:
* Partnerlook Section sorts products by name to display matching items side by side :white_check_mark:

If registered: 
* Product Details allow user to add/remove product to/from wishlist :white_check_mark:

## Highlights
* Products a prominently display :white_check_mark:
* only featured items are rendered :white_check_mark:

## Cart
* Cart is present in Side Drawer Container :white_check_mark:
* Newest Item is always presented on top :white_check_mark:
* Total inkl. Tax & Shipping :white_check_mark:
* Checkout straight from Cart Side Drawer  :white_check_mark:
* Add to cart renders updated cart via Ajax-Request :white_check_mark:
* Increase/Decrease Quantity request via Ajax within Side Drawer Cart :toolbox:
* Remove Items from Cart ia Ajax-Request within Side Drawer Cart :toolbox:
* Reserve requested item & quantity to for 10 Min. to avoid checkouts with unavailable products :toolbox:

If registered: 
* attach cart to userprofile instead of saving to session :toolbox:

## Checkout
* Order summary :white_check_mark:
* Form to enter shipping address :white_check_mark:
* Payment via Credit Card :white_check_mark:
* Users gets order confirmation by mail :white_check_mark:
* general discount codes can be used :toolbox:
* personalized discount codes can be used :toolbox:
* Users receives order updates when order status changes :toolbox:
* Apple Pay integration :toolbox:

If registered: 
* Form is prefilled with available user data :white_check_mark:
* Form data can be saved to userprofile :white_check_mark:

## Sign Up & login:
* Sign up can be undertaken :white_check_mark:
* Sign up also collected first and last name :white_check_mark:
* login can be undertaken :white_check_mark:
* Password reset :white_check_mark:
* Delete account :toolbox:
+ Sign in with apple or google account :toolbox:

## Registered Users: Useraccount
* User can look up saved address information :white_check_mark:
* User can update address information :white_check_mark:
* User can see past orderes :white_check_mark:
* User can enter detail view of past orders :white_check_mark:

## Registered Users: Wishlist
* User can add/remove items to personal wishlist from product details :white_check_mark:
* User can view stored wishlist items :white_check_mark:
* Users can add items to wishlist from product overview :toolbox:
* users can add items and size to wishlist :toolbox:
* users can immediatley transform wishlist into order :toolbox:

## Store Management:
* ... can create/read/update/delete products in Django-Admin-View :white_check_mark:
* ... can create/read/update/delete blogposts in Django-Admin-View :white_check_mark:
* ... can create/read/update/delete FAQs in Django-Admin-View :white_check_mark:
* ... can create/read/update/delete Users in Django-Admin-View :white_check_mark:
* ... Order Management system :toolbox:


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


