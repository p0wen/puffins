# Introduction

For this project different testing approaches where pursued. Core Testing method for The Puffins was manual testing and user testing. Additionally Testcases based on Django TestCase where introduced to this project to support the development process. In addition to testing the code ran through specific validation services to spot any irregularities or syntax errors. On top of that the project was posted to Code Institutes private #peer-code-review Slack Group to gather some more feedback from students and alumnis. The following documentation provides an detailed overview of the defined testcases, the automatic testing setup, validation service results and insights to challenging bugs that were encoutered during the development of this project.

# Table of Content

--> INSERT TABLE OF CONTENT

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
4. Click Userprofile-icon and login with 
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

## 5. Help / Contact Page

### Contact Page through Navbar
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on HELP in Navigation
4. Check that  
   FAQs are diplayed  
   FAQs are categorized  
   Contact form available

### Contact Page - Submit Form
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on HELP in Navigation
4. Fill out Form
5. Submit Form
6. A success message should be presented instead of the form

### Contact Page - Submit Form prefilled
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Login with 
4. Check that Form is prefilled (puffin1@byom.de, Huffin, Puffin)

## 6. Shop

### Shop Categories
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids or Grown Ups
5. Check that products are displayed and the page title shows the Category

### Shop Productline
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Check that only productline items are displayed and the page title shows the Category & Productline

### Shop Partnerlook
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Partnerlook
5. Check that matching products are displayed next to eachother and the page title states "Partnerlook" with the subtitle "T-Shirt & Sweatshirt"

### Sort Products 
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Toggle the Sort switch through all options and check that sorting works accordingly  
    ...Featured Products  
    ...Price
    ...Color
    ...Name 

### Sort Products 
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Check different card design for regular, sale(red) and pre-order(blue) items

### Get Product Details
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

### Get Product Details
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Login with 
4. Click on SHOP
5. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Heart below Add to Cart-Button should be visible

## 7. Highlights

### Get Highlights
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on HIGHLIGHTS
4. Only one Product per row should be shown

## 8. Cart

### Check empty Cart
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on Cart-Icon
4. Side Drawer Cart should open
5. Placeholder "Nothing in Cart" should be displayed 

### Add item to Cart
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Chosen Product should be inside the cart view

### Open Fullpage Cart
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Click below checkout button on Go to Cart
9. Fullpage Cart should open

### Add two items to Cart and check Position
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

### Checkout from Side Drawer Cart
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click on SHOP
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Add Item to Cart
7. Side Drawer Cart should open
8. Press Checkout Button
9. Checkout Page should open

### Checkout from Fullpage Cart
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

### Increase Quantity in Side Drawer Cart
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

### Decrease Quantity in Side Drawer Cart
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

### Remove Item(s) in Side Drawer Cart
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

### Increase Quantity in Fullpage Cart
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

### Decrease Quantity in Fullpage Cart
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

### Remove Item(s) in Fullpage Cart
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

## 9. Checkout

### Checkout AnonymousUser
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

### Checkout registered user

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon and login with 
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

## 10. Sign Up:

### Sign Up
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon
4. Choose Sign Ups
5. Fill out the Form
6. Check if confirmation mail was received
7. Confirm email
8. Login with credentials

## 11. Registered Users: Useraccount

1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on UserAccount-icon
5. Should see Form 
6. Should see Order History

## Registered Users: Wishlist

### Show empty wishlist
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on Heart-icon
5. Should show empty wishlist

### Add product to wishlist
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Login with 
4. Click on SHOP
5. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Choose any product by clicking the image
6. Click Heart below Add to Cart-Button
7. Heart should change from outline to filled

### Show wishlist
1. Open Browser
2. Open [Puffins Page](https://thepuffins.herokuapp.com)
3. Click Userprofile-icon and login with 
4. Click on Heart-icon
5. Should show wishlist with one liked item

## 12. Store Management:

### create/read/update/delete products
### create/read/update/delete blogposts 
### create/read/update/delete FAQs
### create/read/update/delete Users


# User Testing

Besides running through the extensive test cycles documented above the URL from the Heroku deployment was shared with friends and family. The following feedback was collected:

- "Great products"
- "Beautiful design"
- "I wish i could increase/decrease quantity within the sidedrawer cart"
- "Footer looks a little too full"

Following Bugs were identified:
- Side Drawer Cart on iPhone not scrollable :white_check_mark:
- Quantity not shown in Side Drawer Cart :white_check_mark:
- Buttons on Carrousel not inline with button box :white_check_mark:
- Cart Mobile Fullpage not in view :white_check_mark:
- Info Toast behind Navbar :white_check_mark:

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


