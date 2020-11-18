# Introduction

For this project different testing approaches where pursued. Core Testing method for The Puffins was manual testing and user testing. Additionally Testcases based on Django TestCase where introduced to this project to support the development process. In addition to testing the code ran through specific validation services to spot any irregularities or syntax errors. On top of that the project was posted to Code Institutes private #peer-code-review Slack Group to gather some more feedback from students and alumnis. The following documentation provides an detailed overview of the defined testcases, the automatic testing setup, validation service results and insights to challenging bugs that were encoutered during the development of this project.

# Table of Content

- [Introduction](#introduction)
- [Table of Content](#table-of-content)
- [Manual Test Cycles](#manual-test-cycles)
  * [1. Test Navbar](#1-test-navbar)
  * [2. Footer](#2-footer)
  * [3. Landing Page](#3-landing-page)
  * [4. About Page](#4-about-page)
  * [5. Help / Contact Page](#5-help---contact-page)
  * [6. Shop](#6-shop)
  * [7. Highlights](#7-highlights)
  * [8. Cart](#8-cart)
  * [9. Checkout](#9-checkout)
  * [10. Sign Up:](#10-sign-up-)
  * [11. Registered Users: Useraccount](#11-registered-users--useraccount)
  * [12. Registered Users: Wishlist](#registered-users--wishlist)
  * [13. Store Management:](#12-store-management-)
    + [Product Management](#product-management)
    + [Order Management](#order-management)
    + [Blog Management](#blog-management)
- [User Testing](#user-testing)
- [Automatic Tests & Continious Integration](#automatic-tests---continious-integration)
- [Validation Services](#validation-services)
  * [Validation Tools](#validation-tools)
  * [Responsiveness & Rendering](#responsiveness---rendering)
  * [Browser Compatibility](#browser-compatibility)
- [Peer-Code-Review](#peer-code-review)
- [Bug-Log from Development](#bug-log-from-development)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# Manual Test Cycles

## 1. Test Navbar :white_check_mark:

### General Functionalities :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click every nav item

### Logged in and non-logged in users see different options :white_check_mark:

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
4. Click Userprofile-icon and login with 
5. Check that navbar icons changed and the follow are present  
   Useraccount-icon  
   Wishlist-icon  
   Cart-icon  
   Search-icon  

### Searchbar opens below nav when search icon is clicked :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Search-icon
5. Searchbar should open below nav

### Fixed to top and transparent :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Don't scroll check that nav is transparent

### Changes background and font color on scroll  :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Scroll and check that nav background changes to white and font to black

### Changes background and font color if collapsed on small screens :white_check_mark:

1. Open Browser on medium screen
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Don't scroll
4. Click collapse button
5. Check that nav background changes to white and font to black

## 2. Footer :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Scroll to bottom
4. Check that  
   Logo is displayed  
   Quicklinks to products are available  
   Contact details are accessabile 
   Link to About page is present

## 3. Landing Page :white_check_mark

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Check that  
   Caroussel with images is behind nav  
   Check that no more than 4 random Products are displayed  
   Product details can be accessed by clicking the SHOP Button 

## 4. About Page :white_check_mark:

### About Page through Navbar :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on About in Navigation
4. Check that ...  
   Vision is diplayed  
   Short introduction to company is provided

### About Page through Navbar :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Scroll to bottom of page
3. Click on About in Footer
4. Check that same information is present as in Test 4.1

## 5. Help / Contact Page :white_check_mark:

### Contact Page through Navbar :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on HELP in Navigation
4. Check that  
   FAQs are diplayed  
   FAQs are categorized  
   Contact form available

### Contact Page - Submit Form :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on HELP in Navigation
4. Fill out Form
5. Submit Form
6. A success message should be presented instead of the form

### Contact Page - Submit Form prefilled :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Login with 
4. Check that Form is prefilled (puffin1@byom.de, Huffin, Puffin)

## 6. Shop 

### Shop Categories :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids or Grown Ups
5. Check that products are displayed and the page title shows the Category

### Shop Productline :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Check that only productline items are displayed and the page title shows the Category & Productline

### Shop Partnerlook :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Partnerlook
5. Check that matching products are displayed next to eachother and the page title states "Partnerlook" with the subtitle "T-Shirt & Sweatshirt"

### Sort Products (3 :white_check_mark: / 1 :beetle:)
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Toggle the Sort switch through all options and check that sorting works accordingly  
    ...Featured Products :white_check_mark:  
    ...Price :beetle:  
    ...Color :white_check_mark:  
    ...Name :white_check_mark:  

    Finding: Sorting by Price works. However due to the datamodel holding an attribut discount_price and normal price the sorting does not take discount_prices into consideration. This should be fixed by either adjusting the model or finding a way to handle it via a function on the get request.

### Check Product types :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Check different card design for regular, sale(red) and pre-order(blue) items

### Non-logged-in user: Get Product Details :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. New page should open
7. Page should contain  
   Product image  
   Descripton  
   Size Options
   Add to Cart Button  
   Material information  
   Return & Delivery Information

### Logged-in-user: Get Product Details :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Login with puffin1@byom.de pw: testuser1
4. Click on SHOP
5. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Heart below Add to Cart-Button should be visible

## 7. Highlights :white_check_mark:

### Get Highlights :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on HIGHLIGHTS
4. Only one Product per row should be shown

## 8. Cart :white_check_mark:

### Check empty Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on Cart-Icon
4. Side Drawer Cart should open
5. Placeholder "Nothing in Cart" should be displayed 

### Add item to Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Chosen Product should be inside the cart view

### Open Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Fullpage Cart should open

### Add two items to Cart and check Position :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Continue shopping by clicking on the grey overlay or on to the Close button in the top right
9. Cart should Close
10. Choose another product
11. Add Item to Cart
12. Side Drawer Cart should and last added item should be on top

### Checkout from Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press Checkout Button
9. Checkout Page should open

### Checkout from Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Fullpage Cart should open
10. Press Checkout Button
11. Checkout Page should open

### Increase Quantity in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "+" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Quantity should be increased by 1

### Decrease Quantity in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "-" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Quantity should be decreased by 1

### Remove Item(s) in Side Drawer Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press "x" Button in Side Drawer Cart
9. Should be redirect to Fullpage Cart
10. Product should be removed from Cart

### Increase Quantity in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "+" Button
11. Page should be reloaded and quantity increased by one

### Decrease Quantity in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "-" Button
11. Page should be reloaded and quantity decreased by one

### Remove Item(s) in Fullpage Cart :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Should be redirect to Fullpage Cart
10. Press "x" Button
11. Page should be reloaded and item should be removed from cart

## 9. Checkout :white_check_mark:

### Checkout AnonymousUser :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click Checkout-Button
9. Should be redirected to checkout page
10. Form for address details & Order Summary should be displayed
11. Fill in form & use test credit card (4242 4242 4242 4242)
12. Submit order
13. Loading animation should be displayed
14. Checkout success page should be shown

### Checkout registered user :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon and login with puffin1@byom.de pw: testuser1
4. Click on SHOP
5. Click Kids - T-Shirt or Grown Ups - Sweatshirts
6. Choose any product by clicking the image
7. Add Item to Cart
8. Side Drawer Cart should open
9. Click Checkout-Button
10. Should be redirected to checkout page
10. Form for address details should be prefilled & Order Summary should be displayed
11. add test credit card (4242 4242 4242 4242)
12. Submit order
13. Loading animation should be displayed
14. Checkout success page should be shown

## 10. Sign Up :white_check_mark:

### Sign Up :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon
4. Choose Sign Ups
5. Fill out the Form
6. Check if confirmation mail was received
7. Confirm email
8. Login with credentials

## 11. Registered Users: Useraccount :white_check_mark:

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on UserAccount-icon
5. Should see Form 
6. Should see Order History

## Registered Users: Wishlist :white_check_mark:

### Show empty wishlist :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on Heart-icon
5. Should show empty wishlist

### Add product to wishlist :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Login with 
4. Click on SHOP
5. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Click Heart below Add to Cart-Button
7. Heart should change from outline to filled

### Show wishlist :white_check_mark:
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on Heart-icon
5. Should show wishlist with one liked item

## 12. Store Management :white_check_mark:

### Product Management :white_check_mark:

#### Create Product :white_check_mark:
#### Read Product :white_check_mark:
#### Update Product :white_check_mark:
#### Delete Product :white_check_mark:

### Order Management :white_check_mark:

#### Create Order :white_check_mark:
#### Read Order :white_check_mark:
#### Update Order :white_check_mark:
#### Delete Order :white_check_mark:

### Blog Management :white_check_mark:

#### Create Post :white_check_mark:
#### Read Post :white_check_mark:
#### Update Post :white_check_mark:
#### Delete Post :white_check_mark:

# User Testing

Besides running through the extensive test cycles documented above the URL from the Heroku deployment was shared with friends and family. The following feedback was collected:

- "Great products"
- "Beautiful design"
- "Footer looks a little too full"

Following Improvements/Features/Bugs were identified:
* Feature Requests  
  * Feature request: I wish i could increase/decrease quantity within the sidedrawer cart :white_check_mark:
* Improvement
    * Cart on Mobile view hidden. As an idea for a later release the logo and text logo would move to the center. Moving the Burger-Menu to the left side of the screen and adding the cart symbol to the right top corner. :toolbox:
* Bugs
    * Quantity not shown in Side Drawer Cart :white_check_mark:
    * Buttons on Carrousel not inline with button box :white_check_mark:
    * Cart Mobile Fullpage not in view :white_check_mark:
    * Info Toast behind Navbar :white_check_mark:
    * Adding a Product to the cart and using the back button in browser or the implemented backbutton does not refresh the page. Therefor the cart does not signal that the user has something in the cart. Couple of solutions found on Stackoverflow were tested but none could solve the issue. This bug is still pending and should be fixed in the next release. :toolbox:

# Automatic Tests & Continious Integration

A basic set of test using the Django TestCase integration were created to support the testing and development process and gain practical knowledge in this field. Test were written for the following apps:

- About (Views) - 100% Coverage
- Blog (Models & Views) - 100% Coverage
- Contact (Forms 100%, Models 100%, Views 54%)
- Useraccount (Forms 81%, Models 100%, Views 65%)
- Wishlist (Models 100% & Views 58%)

More test need to be written to reach a 100% test coverage. Furthermore, [Travis CI](https://travis-ci.org/github/p0wen/puffins) used to allow continious integration patterns in combination with Heroku. Travis CI is an open source software for continious integration.

Build Status:

[![Build Status](https://travis-ci.org/p0wen/puffins.svg?branch=master)](https://travis-ci.org/p0wen/puffins)

# Validation Services

## Validation Tools
### [W3C Markup Validation Service](https://validator.w3.org)
All pages incl. sub-pages were processed through the [W3C Markup Validation Service](https://validator.w3.org). The validation revealed some missing ```alt=""``` statements, stray ```<div>```'s and conventions regarding the use of ```<span>``` in combination with ```<hr>```. The findings were all resolved and no more issues were found by the [W3C Markup Validation Service](https://validator.w3.org).
### [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/)
The whole css file ran through the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). After taking care of some minor errors and cleaning up the css 5 Errors are still reported. These Errors were accepted since they mark the use of the javascript injected dynamic ```--vh``` variable in combination with the ```calc()``` operation. Furthermore 18 Warnings were accepted. The 10 of the 18 warnings also relate to the dynmic height view-height variable. And the other 8 warnings inform about same colors on 2 classes ```.allauth-form-inner-content button``` and ```.allauth-form-inner-content input[type="submit"]``` which was also accepted in this case.
### [JS Hint](https://jshint.com)
All *.js files were checked with the service of [JS Hint](https://jshint.com). By using this service some bugs like wrong use of ```&&``` in if functions and missing `;` were identified and solved.
### [PEP8 Online](http://pep8online.com)
All *.py files were checked with the service of [PEP8 Online](http://pep8online.com). The files looked all good and no error was reported.
## Responsiveness & Rendering
The site was created with the mobile first approach in mind. The following devices / device sizes were used for testing the responsiveness:
* iPhone 11 Pro 
* iPad 10,2"
* MacBook Pro 13"

## Browser Compatibility
The site was tested on the following Browsers:
* [Apple Safari](https://www.apple.com/safari/) 
* [Google Chrome](https://www.google.com/chrome/)
* [Brave Broser](https://brave.com/)
* [Microsoft Edge](https://www.microsoft.com/edge)

On all browsers full site compatibility was identified based on the test cases.

# Peer-Code-Review

The project was peer-reviewed by students from code institute. Feedback was given on the readme files and the code. 

# Bug-Log from Development

The following bugs were identified and mainly fixed during development:
1. Updating userprofile even if checkbox is unchecked on Checkout form:  

   This issue was identified during the extensive testing protocoll and took a while to solve. The problem was that the used JavaScript call to check if the checkbox is checked or unchecked always returned true. Furthermore, the python code didn't identify the javascript `true`/`false` response as `True` or `False`. Therefore the functions did not process the given information as intended. The following lines were introduce to make the function work as intended:
   ```
   stripe_elements.js
   var saveInfo = $('#id-save-info').is(':checked');
   ```
   ```
   webhook_handler.py
   if save_info == "true":
   ```
2. Webhooks for orders  without the optional streetaddressline2 filled out were failing. Therefore customers who didn't provide a line2 street address were not receiving their order confirmation. The problem laid in the model definition. By allowing `null` to be `true` on `street_address2` the webhooks were processed without problems.
3. Adding products to a wishlist if no item was added before on a fresh user failed in the beginning. The solution was to use the `get_or_create` method and check if the object was created or already existed.  
4. Product images were not displayed when using the `{{MEDIA_URL}}` template tag. This was solved by extensivly checking the settings.py and by realizing that the ```django.template.context_processors.media``` was missing in the templates setup. 
5. Importing fixtures to postgres db led to some troubles. This was solved by making sure the charfields are set correct and that especially on long descriptions it makes sense to use TextField.


