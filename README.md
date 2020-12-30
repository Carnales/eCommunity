# eCommunity
The next generation of local eCommerce for the next generation of Communities. This a hackathon project for NChack 2020.

When we think of winter, we think about two things: the holidays, and community. While many rejoice during winter with Christmas and gifts, many others find it to be trying times for them and their business. As a result, we decided to unite the local community under one spectacular online store where local businesses can spread holiday love with products for sale, and families can help local businesses out by buying from the local stores for holiday shopping, aided through this online platform, the winter eCommunity.

## Setup

* Download the project either as a zip or through GitHub Desktop.
* In your CMD terminal, "cd" into the root directory.
* First, you have to activate the environment to download all required dependencies. To do so, run:
```
\env\Scripts\activate.bat
```
Note: You should see (env) on the left of your terminal now.
* Now, "cd" into the eCommunity folder and run the django server through:
```
python manage.py runserver
```
Note: If you get windows socket errors, run 'python manage.py runserver 8080' instead to run it on a different port.
* It should be all ready, now just open your favourite browser (it better not be IE) and open: "localhost:8000" or "127.0.0.1:8000".

## Fun Facts
* We wrote it with full backend support through python and django, and front end with html/css/js
* You can change the quantity of items in the cart as well!

## Guide

### First Time User
1. Register as a User by pressing the Register button on the Navigation bar. Upon a successful registration, the page will redirect to a completed registration. You can not add to cart unless you are a user!
![Register](images/left-navbar.png?raw=true "Register")
![Forms](images/forms.png?raw=true "Forms")
2. Once Registered, you are free to explore the shops in the homes page.
![Store](images/store.png?raw=true "Store")
3. If you are interested in one of the products listed, click on add to cart.
![Product](images/product.png?raw=true "Product")
4. Once all items of interest have been added, proceed to the sleigh icon. You will be directed to the cart page.
![Cart](images/cart.png?raw=true "Cart")
5. After confirming each quantity and your total, click on the checkout button to complete your order.
6. Your order is now complete!

### Deleting Your Account
1. If you no longer want to associate with eCommunity press the "Delete Account" button on the navigation bar.
![Delete](images/left-navbar.png?raw=true "Delete")
2. You will be logged out and **your account info will be deleted**. However, keep in mind that without an account you are unable to shop.

## Post NC-Hack
-  Add Employee Support
-  Add Business Page Backend Support
-  Add Customer Support Page
-  Add PayPal Integration
-  Add User Businesses Store Pages
-  Add User to Business Owner Communication
-  Add a search feature
-  Add a map feature

## Code Bases Implemented and reworked from:
  - "Bootstrap 4 Navbar with Icon Top" - https://bootsnipp.com/snippets/nNX3a

  - "Bootstrap Weather Card UI" - https://bootsnipp.com/snippets/Bq1eE

  - "Bootstrap cards" - https://codepen.io/maryj25/pen/axBNVO

  - "BOOTSTRAP STATIC HEADER" - https://bootstrapious.com/p/bootstrap-static-header

  - "cart.html" - https://github.com/divanov11/django_ecommerce_mod5/blob/master/store/templates/store/cart.html

  - Bootstrap Documentation

## Example Stock in Stores Obtained from:

### John's Family Ski Rental
    - "Men's Winter Coat" - https://www.grailed.com/drycleanonly/winter-coat-style-guide

    - "Children's Red Skis" - https://s3-us-west-2.amazonaws.com/usedphotosna/95604602_614.jpg

    - "John's Store banner" - https://image.shutterstock.com/image-photo/ski-skier-snow-fun-family-260nw-220318912.jpg

    - "Ski Helmet" - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thesnowcentre.com%2Fsnowsure%2Fnews%2Fdo-i-need-a-ski-helmet&psig=AOvVaw3izw7T21QJOOwvBl0p8niE&ust=1609376010143000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNiZ0v--9O0CFQAAAAAdAAAAABAD

    - "Elite Ski Goggles" - https://www.evo.com/goggles/smith-io-mag?avad=52463_b1f051f0d&a=Avantlink&utm_source=AL&utm_medium=Affiliate&utm_campaign=38931

    - "Burton GORE-TEX Gloves" - https://www.evo.com/gloves/burton-gore-tex#image=152944/641953/burton-gore-tex-gloves-.jpg

### Joseph's Toy Store
    - "Joseph's Toy Store" - https://momsla.com/wp-content/uploads/2017/11/Landis-labrinth-larchmont.jpg

    - "Toy store banner" - https://i.pinimg.com/originals/be/d5/fd/bed5fd1802894bad474e46c72033d10e.jpg

    - "Nutcracker" - https://images.squarespace-cdn.com/content/v1/57642bcbff7c507e598291d9/1567100154463-F7HNMMQVA3SNI1T7YML7/ke17ZwdGBToddI8pDm48kOI1i559IYU_WKaTq-JB9vt7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0p4XabXLlNWpcJMv7FrN_NLLxAnkhViNZICZamvPltgLQld8UDTdlTLjiMT25Fg2ew/3.+Nutcracker+Dec.+12-15-+iStock.jpg

    - "Yoda" - https://cnet3.cbsistatic.com/img/-qrd4awRVDn488rVBFRlSwhx7ds=/1200x675/2020/10/28/5a601f4a-06c8-4374-b10d-9f07fe183390/babyyoda-target-1.png

    - "McDonald's Set" - https://i.ytimg.com/vi/xzaNqjc4fkE/maxresdefault.jpg

    - "Blue Power Ranger" - https://www.cnet.com/news/blue-power-ranger-billy-cranston-ranger-slayer-join-lightning-collection/

### Merill's Bakery
    - "Bakery Banner" - https://images.unsplash.com/photo-1483695028939-5bb13f8648b0?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cGFzdHJ5fGVufDB8fDB8&ixlib=rb-1.2.1&w=1000&q=80

    - "Bakery in snow" - https://deliveryconcepts.com/wp-content/uploads/2019/10/automobile-automotive-bakery-730129-1024x766.jpg

    - "Mousse Pastries" - https://www.puffpastry.com/recipe/white-chocolate-mousse-pastries/

    - "Blueberry Pies" - https://www.justataste.com/wp-content/uploads/2016/04/fruit-cream-cheese-breakfast-pastries-recipe.jpg

### Yolanda's Gingerbread House
    - "Yolanda Profile" - https://www.chefpassport.com/chefListing/Yolanda-Wu

    - "Yolanda's Banner" - http://www.teambuildingsolutions.co.uk/activities/gingerbread-house-making

    - "Gingerbread Cookie Cutter" - https://www.michaels.com/gingerbread-man-cookie-cutter-by-celebrate-it-christmas/10645624.html?r=g

    - "Gingerbread House Set" - https://www.amazon.com/Wonka-Gingerbread-Cottage-Kit/dp/B00GAP5SZG

    - "Kitchen Utensils" - https://www.pinterest.com/pin/827958712724684712/

### Uncle Rick's Art Studio

    - "Uncle Rick's Studio" - https://www.hgtv.com/sweepstakes/hgtv-urban-oasis/2017/hgtv-urban-oasis-2017-art-studio-pictures

    - "Uncle Rick's Banner" - https://www.christies.com/departments/Swiss-Art-54-1.aspx

    - "Tides of War" - https://www.etsy.com/ie/listing/585187578/abstract-painting-art-on-16-x-20-canvas

    - "Orwellian Tulipians" - https://cgmodernart.com/abstract-art-paintings/large-abstract-art-on-canvas-yellow-tulips

    - "Freudian Man" - https://www.kentpaulette.com/product/dream-bear/

    - "Wave of Guilt" - https://www.dna11.com/products/fingerprint-portraits
