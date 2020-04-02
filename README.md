# Stephens Pop Shop

This is my fourth milestone and ironically my fourth attempt.

As this is my fourth attempt I will include links to my previous attempts that can be found at

- <https://github.com/jjackson19862017/PopWorld>
- <https://github.com/jjackson19862017/popworld2>
- <https://github.com/jjackson19862017/popworld3>

I will be using previous code, from my past attempts to save me time.  As I only have 3 days to complete this project and submit it in for assessment.  I have started again, has I was trying to be clever and do everything in my head.  I realise my tables could be managed and designed better.  I actually went old school and wrote my tables out and drew the links.  Visually seeing it was better for me to understand where I could of gone wrong previously.

## Lets Get Down To Business

For my Fourth and Final Milestone Project have choosen to build a project based on an auction website involving Pop!Vinyl's.  The goal of the website is for the Owner to advertise his Pop!Vinyl collection and sell them to the public involving either bidding for items or buying them out-right.

I will set up an authentication and authorisation.  Where only registered users can bid and buy items that are up for auction.

When the buyers come to purchase their goods, they will be using the Stripe Payment Method.

## Project Brief

- Earn money on selling the toys known as Pop!Vinyl's (the site owner is the seller)

- Create an online store focused on selling Pop!Vinyl's, from different series to the highest bidder.

- Allow users to search for Pop!Vinyl's based on various fields.

- Allow users to see the price, image and other basic details about an Pop!Vinyl.

- Allow users to bid on items, or pay a higher price to purchase them immediately. Users have to be registered for this.

### Advanced potential feature (nice-to-have)

Allow registered users to write reviews about the Pop!Vinyl's, only if they purchased them.

Expand the search functionality to allow users to sort results based on price, character and other parameters in both ascending and descending order.

Include pagination and/or other dynamic display actions using javascript or bootstrap.

Use javascript polling to update the page whenever there's a new bid.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

| Technology      | How it was used                                                 | Website                                            |
| :--------------:|-----------------------------------------------------------------|---------------------------------------------------:|
| HTML            | Backbone of everything                                          | <https://www.w3schools.com/html/default.asp>         |
| CSS             | Styling for the MATERLIZE to work on                            | <https://www.w3schools.com/css/default.asp>          |
| MATERLIZE       | A modern responsive front-end framework based on Material Design| <https://materializecss.com/>                        |
| JAVASCRIPT      | Used for some functionality on the website                      | <https://www.w3schools.com/js/default.asp>           |
| PYTHON          | Used for the main functionality on the website                  | <https://www.w3schools.com/python/default.asp>       |
| SQLITE3         | Light Local Database                                | <https://www.sqlite.org/index.html>       |
| POST GRE           | Non-Relational Database                                         | <https://cloudmongo.com>                             |
| DJANGO          | Web Framework                                                    | <https://www.djangoproject.com/>|
| HEROKU          | Cloud Platform to Host the Django App                            | <https://id.heroku.com/login>                        |
| TRAVIS          | Testing Platform                                                 | <https://www.travis-ci.org/>                        |
| GITHUB          | Stores my work so that other people and myself can reference it | <https://www.github.com>                             |
| GITPOD          | An IDE allowing me to code on any browser                       | <https://www.gitpod.io>                              |
| VSCODE          | An IDE allowing me to code on my computer                       | <https://code.visualstudio.com/>                     |
| SLACK           | An chat application to allow others to communicate              | <https://slack.com/intl/en-gb/>                      |
| Stripe JS       | For easy payment when user select paynow option on all screen sizes | <https://stripe.com/ie>               |

## Places I Have Looked For Help

- Django Documentation - <https://docs.djangoproject.com/en/3.0/>
- Pop In a Box - <https://www.popinabox.co.uk/> - These were used for the Product Images

## Timeline

### Thursday 26th March 2020

Started project for a fourth time, going to commit my readme.md and env.py and gitignore as my --> "Initial Commit".

Time to create my project called "popshop", and change the settings file to hide hidden keys etc.

I will also create the static and media folder structure.

--> "Project Setup"

Create accounts for users.

Created Superuser

--> "Accounts App Created"

Create Products app for Products to populate with.

Created Templates folder as I forgot to do that when I was creating my static folder.

--> "Products App Created"

Create Search app for users to search for potential products.

--> "Search App Created"

Create Cart app for users to buy products.

--> "Cart App Created"

Create Checkout app for users to make payments.

--> "Checkout App Created"

Create Auction app for the owner to create auctions.

--> "Auction App Created"

Create Bids app for the users to bid on auctions.

--> "Bid App Created"

So now I am back to where I started however there are a few adjustments I have to make due to the fields changing tables.

Also got rid of home redirect as I am not using a home app this time around.

--> "Field Updates"

While building and testing my website, I have found it annoying to remember who I am logged in as, so I have modified the base.html to run an if statement to see if I am a superuser.  If that is true then the navbar will turn Red.

I have also moved around the links on the navbar.

--> "Navbar Update"

I thought it would be some nice feedback for the user, if the loops were empty.  Ie no products or auctions.  I found the solution on <https://docs.djangoproject.com/en/1.11/ref/templates/builtins/>

I also changed the way the cart and checkout looks, they now appear as tables so it looks like an invoice.

--> "Empty Lists UI Update"

I have found a problem with paying for things with Stripe so I am watching the videos again.

My jquery and the stripe js was being loaded out of order.

--> "Fixed Stripe Payments"

I have changed everything from Pop World to Pop Shop.

I have also hidden the cart if it is empty.  This is to stop people from openning an empty cart.

--> "Shop Update"

I have got the bids to work with the new field in the other table

--> "Bids Working"

Safe this for later

            {% if i.user_id.username != user.username %}
            <form action="{% url 'bid_on_auction' %}" method="POST">
                {% csrf_token %}
                <div class="input-group">
                    <input type="hidden" name="product_id" value={{ auction.product_id.id }} />
                    <input name="UpBid" type="number" min="5" max="9999" class="form-control" placeholder="Enter minimum £ 5">
                    <span class="input-group-btn"><button class="btn btn-success">Increase Bid</button></span>
                </div>
            </form>
          {%else%}
            <p class="product-text text-center">You cannot bid again, <br>Wait till someone else bids.</p>
            {%endif%}

### Saturday 28th March 2020

I tried to see if I could display my bid data on my auction site, however after many tries.  I created a field in the auction model that is updated by the open_auction

--> "Auction Models Updated"

Updated some links, and changed the base.html to reflect open and closed auctions.

Researched Countdown Timers for JS <https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_countdown>

Unfortunately can't get it to work at the present time, will focus on the task I have been putting off and thats getting my winning bid to purchase.

Im so close to getting it working, just need some help.

--> "Nearly there with putting a winning bid into a cart"

I have spent nearly 2 hours looking on how to put this PRICE from add_to_cart view into the cart_contents context

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    price = float(request.POST.get('price'))
    print("id: " + str(id))
    print("price: " + str(price))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity  
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

  def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        
        price = product.instant_buy_price

        total += quantity * price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        print("product: "+str(product))
        print("total: "+str(total))
        print("product count: "+str(product_count))
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}

Thank you Anne and Tim about sessions, I have got further now

--> "Session Price"

### Sunday 29th March 2020

Updated the Bid.html, to reflect if you have won the auction or not and if you have gives you the chance to pay for your win.
Updated the auction.html, to reflect if you have placed the highest bid or not and if you losing the auction, it gives you chance to bid again.

Updated the views.py in auction to reflect what user has placed a bid.

Tested my new changes with logging in as different users and seeing the outcome on the website.

--> "Bidding Winner Updated"

The Winning Bid button adds, the winning bid to a cart and sends you to a winning bid checkout.

--> "Winner to Checkout"

I now need to figure out is how to delete, an auction once its been won and paid for???

I have also found a problem with my cart as it only allows one newprice, so if there were multiple items in the cart they would all get the same price.

--> "Problems"

### Monday 30th March 2020

Fixed the code so that either Products and Winning Bids will goto the cart.

The only issue, which I know I dont have time to fix is that you can't mix the two types of products, because otherwise the cart won't display the right prices.

--> "Bids and Products Purchasing Working"

Updated the Winning Bid Checkout on looks and modified the Models.

--> "Checkout Update"

Updated the HTML to be more friendly for smaller devices.

--> "UX Friendly"

Updated the Bidcheckout with the ability to delete auctions on successul payments.

My first test deleted all auctions, however in my haste I had selected all auctions.  So I confined my parameters to product id's.

Done

--> "Auction Deleting"

Fixed Two Decimal place in newprice from bidding.

When you open auctions it searches for any closed auctions and changes them to closed, so the user only sees open ones.

--> "Tweaks"

While on Call with Mentor my checkout payment method broke, hes the fix.

--> "Checkout Fixed"

IDEA: Allowing the owner to delete any auctions that he wants to, just incase they have made an error or theres a stock error.

Complete IDEA

--> "Cancel Auction Button"

IDEA: change widget for date and time selector.

I googled a date time picker, I have saved it for now but I dont really like it.

### Tuesday 31st March 2020

I have found a better date time picker, <https://pypi.org/project/django-bootstrap-datepicker-plus/>

Unfortunately couldnt get it working so Plan C <https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django/49064892>

Plan D would work either, you would think that using the in-built date picker would work but NO.

I have spent nearly 6 hours looking for a date picker, to no success.  So instead of the User making an error inputing the date and time.  I have just set a 7 day auction.

--> "Seven Day Auction"

When I tried to log out of my user there came an error about "conversion from dict to Decimal is not supported".

This was the code that was entered when I fixed my decimal and rounding.

So I have created a fix for it.

I have also commented on my code for easy reading.

--> "Decimal Fix, Code Commenting"

Now commenting on code inside my django project and testing anything that needs testing.

#### Accounts

##### Templates

- Index.html: Added Comments
- Login.html: Added Comments
- Profile.html: Added Comments
- Register.html: Added Comments

###### Testing - Index.html

Clicked "Login"     > Took me to Login Screen       >   PASS
Clicked "Register"  > Took me to Register Screen    >   PASS

###### Testing - Login.html

Logged in with known user > PASS
Tried to Login with wrong Password > PASS (Error Message)

###### Testing - Register.html

Create new user     > Filled in details > FAIL (Reverse for 'home' not found. 'home' is not a valid view function or pattern name.)

Create new user     > Filled in details > PASS

#### Auctions

- addauctions.html: Added Comments
- auctions.html: Added Comments, Removed Debug information that End User didn't need to know or see.

##### Testing - addauctions.html

Choose Product for auction > Clicked Start > PASS
Choose Same Product for auction > Clicked Start > FAIL (Can't have the same product up for auction)
Choose Same Product for auction > Clicked Start > PASS (Error Message is present, thank you to <https://youtu.be/wVnQkKf-gHo> for the refresh and understanding)

##### Testing - auctions.html

From previous test above > Open Auctions appearing on page > PASS
Try to Increase Bid > Raise by £5 > PASS
From Previous Test, to stop users bidding again until someone else has bidded it takes away the UpBid Form. > PASS
From Previous Test, Bidding is available to me because I Logged out as the superuser into a different user account > PASS
Try to Bid Nothing > FAIL (invalid literal for int() with base 10: '', Fixed with HTML Required Form Validation)
Try to Bid Nothing > PASS (Validation Message)
As Superuser, Cancel Auction > PASS
After all auctions have been Cancelled, Option to start new auction appears > PASS
If auction has ended then it will update the auction table and that auction will not appear > PASS

#### Bids

- bid.html: Added Comments, IDEA: If winner doesnt want it just cancel the Auction.

##### Testing - bids.html

Click Pay > Takes me to BidCheckout > PASS

#### Cart

- cart.html: Added Comments

##### Testing - cart.html

Change Quantity to 3 > PASS (Quantity and Total Changes)
Change Quantity to 0 > PASS (Empties Cart)
Click on Checkout > PASS (Takes me to Checkout)

#### Checkout

- bidcheckout.html: Added Comments, Also cleaned up the UI
- checkout.html: Added Comments, Also cleaned up the UI

##### Testing - bidcheckout.html

Fill in details and Card Details 4242424242424242 CVV 111 > We have paid for the Bid and the Auction Deletes itself > PASS
Blank Forms, Validation should run > PASS
Fill in details and Card Details 4242424242424242 CVV 111, However the expiry date had passed > PASS (Wouldn't send form)

##### Testing - checkout.html

Fill in details and Card Details 4242424242424242 CVV 111 > We have paid for the Bid and the Auction Deletes itself > PASS
Blank Forms, Validation should run > PASS
Fill in details and Card Details 4242424242424242 CVV 111, However the expiry date had passed > PASS (Wouldn't send form)

#### Products

- products.html: Added Comments
- addproducts.html: Added Comments

##### Testing - products.html

Left Quantity blank, Validation should run > PASS
Value -1 Quantity, Validation should run > PASS
Value 4 Quantity > PASS (Took me to cart, don't like that going to change it to stay on the products page.)
Value 4 Quantity > PASS (Added product to cart and told user by a message.)

##### Testing - addproducts.html

Filled out all information on the page > PASS (Added Product, however I realised there is no Validation.)
Filled out all information on the page the same Name as previous product, this should produce a Validation Error > PASS (No two products can have the same name.)
Left the form Blank, Validation should run > PASS (Required field for Name.)
Filled in the following fields, Name, Description and Character > PASS (I would prefer a default image if one is not provided.)
Filled in the following fields, Name, Description and Character > PASS (Default image is used if one isn't submitted.)

#### Base

- base.html: Added Comments

##### Testing - base.html

Product Search - "Ku" > PASS (Returns Goku)
Product Search - "Go" > PASS (Returns four items with go in them)
Product Search - "" > PASS (Returns All Products)

--> "Commenting Code and Testing"

### Thursday 2nd April 2020

While I was doing my testing, I thought about CRUD.  Am I for filling all the criteria.

#### Create

- Users
- Products
- Auctions
- Bids

#### Read

- Users
- Products
- Auctions
- Bids

#### Update

- Auctions
- Bids

#### Delete

- Products
- Auctions

Should I have an option to delete products?

--> "CRUD"

Setup for Heroku & Postgres

--> "Setup for Heroku & Postgres"

