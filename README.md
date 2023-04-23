# Furniture Restoration Collective

The Furniture Restoration Collective website is primarily a Business to Consumer (B2C) E-Commerce website. The site has two main functions.  Firstly, it allows visitors to browse and purchase furniture products restored by a group of craftspeople.  Secondly, visitors can get a quote for a restoration project they may have in mind.  If the user wishes, the quote can also be processed and an order placed for the restoration work to be done.  A registered user can add a review for the services they have received.  The site administrator can then choose whether to add the review to the main web page for others to see.  Visitors can choose to signup to the mailing list to take advantage of offers and receive the newsletter.  Site administrators can create, read, update and delete products through the user interface.  The site administrator can also delete a product from the product detail page.

![Responsive Mockup](/documentation/screenshots/am-i-responsive.png)

The live site is available for use on [Heroku](https://furniture-restoration.herokuapp.com/).

## UX

### Strategy

__Agile__

This project uses the Agile methodology presented on the GitHub platform. There are 10 epics shown as milestones and 34 user stories shown as issues in GitHub. These user stories are split into [four project iterations](https://github.com/teresabowe/furniture-restoration-collective/projects?query=is%3Aopen). The aim is to deliver a usable product at the end of each iteration.

__Project Goal__

The goal of the project is to create a website to allow users to purchase a piece of furniture that has been restored or to get a quote for a restoration project they may have.

A typical user is someone:

- who is visiting and wishes to understand the purpose of the site
- who is visiting and wants to purchase or have a furniture piece restored
- who is visiting and wishes to gear about offers and news
- who is registered has previously placed an order and wants to add a review
- who is registered has previously placed an order and wants see a list of their orders
- who is an office manager and wants to manage products on the website
- who is an office manager and wants to manage reviews on the website
- who is an office manager and wants to manage crafters on the website
- who is an office manager and wants to manage quotations on the website

Key features identified are:

- Landing page demonstrating the products and services on offer 
- Site administration facility to manage products, reviews and crafters
- User signup and authentication
- Email signup for offers and news
- User order management
- A checkout facility for payments

__Marketing Strategy__

Marketing strategy.

### Scope

The initial scope for this project is documented below in the epics and stories. Each user story has a flag indicating prioritisation and implementation status. There is also a link to each user story in GitHub.

__Epics and User Stories__

EPIC: Site Landing Page

User Stories:

- As a site visitor, I can access the landing page so that I can understand the purpose of the site and take appropriate actions (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/34" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/34/hovercard">#34</a>

EPIC: User Authentication

User Stories:

- As a site visitor, I can register on the site so that I can access the site services and view my profile (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/1" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/1/hovercard">#1</a>

- As a registered user, I can trigger an email confirmation after registration so that I understand that my account is registration is complete (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/2" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/2/hovercard">#2</a>

- As a registered user, I can login and logout of my account so that access my account information (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/3" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/3/hovercard">#3</a>

- As a registered user, I can view my profile so that review my purchase history (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/4" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/4/hovercard">#4</a>

- As a registered user, I can reset my password so that access my account information and keep my account secure (must-have/not complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/5" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/5/hovercard">#5</a>

EPIC: Manage Products

User Stories:

- As a shop owner, I can add products so that I can keep my store up to date with available products (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/6" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/6/hovercard">#6</a>

- As a shop owner, I can view products so that I can see what is available in my store currently (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/7" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/7/hovercard">#7</a>

- As a shop owner, I can update products so that I can ensure the latest product information is shared with customers (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/8" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/8/hovercard">#8</a>

- As a shop owner, I can delete products so that I can ensure the product inventory is up to date (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/9" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/9/hovercard">#9</a>

- As a shopper, I can view product details so that I can review the price, and description, understand the background of the product, learn about the craftsperson, and view the product image (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/11" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/11/hovercard">#11</a>

- As a shopper, I can view the shopping basket total so that I can see how much I need to pay (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/13" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/13/hovercard">#13</a>


EPIC: Product Search and Sort

User Stories:

- As a shopper, I can search for a product by name or description so that I can find what I need to purchase (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/14" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/14/hovercard">#14</a>

- As a shopper, I can sort products by price and name so that I can find the most appropriately priced product for my needs or find by name (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/15" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/15/hovercard">#15</a>

- As a shopper, I can sort a selected category of product by price and name so that I can find the most appropriately priced product for my needs or find by name for the selected category (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/16" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/16/hovercard">#16</a>

EPIC: Shopping Cart

User Stories:

- As a shopper, I can view items in the shopping cart so that I can view total amount due and a list of items I am purchasing (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/17" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/17/hovercard">#17</a>

- As a shopper, I can enter payment details so that I can checkout as quickly and securely as possible (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/18" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/187/hovercard">#18</a>

- As a shopper, I can view order confirmation so that I can check that I have made the correct purchase (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/19" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/197/hovercard">#19</a>

- As a shopper, I can receive an email to confirm the purchase is complete so that I can I have my own record of the transaction (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/20" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/20/hovercard">#20</a>

EPIC: Quote for Custom Restore

User Stories:

- As a site visitor, I can get a quotation so that I can find out the cost of my restoration project (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/35" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/35/hovercard">#35</a>

EPIC: Setup UI to Manage Products

User Stories:

- As a shop owner, I can add products in user interface so that I can easily keep my store up to date with available products (should-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/31" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/31/hovercard">#31</a>

- As a shop owner, I can delete products in user interface so that I can ensure the product inventory is up to date (should-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/32" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/32/hovercard">#32</a>

- As a shop owner, I can view products in User Interface so that I can review the price, and description, understand the background of the product, learn about the craftsperson, and view the product image (should-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/33" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/33/hovercard">#33</a>

- As a shop owner, I can edit products in user interface so that I can easily keep my store up to date with available products (should-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/36" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/36/hovercard">#36</a>

EPIC: Crafter Profiles

User Stories:

- As a shop owner, I can add a crafter profile so that I can record information about the crafter community (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/25" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/25/hovercard">#25</a>

- As a shop owner, I can view a crafter profile so that I can ensure the crafter profile is up to date (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/26" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/26/hovercard">#26</a>

- As a shop owner, I can update a crafter profile so that I can keep the crafter profile up to date (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/27" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/27/hovercard">#27</a>

- As a shop owner, I can delete a crafter profile so that I can remove a crafter profile that is no longer relevant (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/28" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/28/hovercard">#28</a>

EPIC: Product Testimonials

User Stories:

- As a shopper, I can add a product testimonial so that I can give product feedback (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/29" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/29/hovercard">#29</a>

- As a shop owner, I can post a product testimonial so that I can share product feedback (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/30" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/30/hovercard">#30</a>

EPIC: Blog Posts

User Stories:

- As a shop owner, I can add a blog post so that I can inform my users about news, products and the crafter community (could-have/ not complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/21" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/21/hovercard">#21</a>

- As a shop owner, I can view a blog post so that I can ensure the contents are accurate and up to date (could-have/ not complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/22" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/22/hovercard">#22</a>

- As a shop owner, I can update a blog post so that I can keep the blog up to date (could-have/ not complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/23" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/23/hovercard">#23</a>

- As a shop owner, I can delete a blog post so that I can keep the blog up to date (could-have/ not complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/24" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/24/hovercard">#24</a>


### Structure

The website has 12 key user pages currently. The following pages are open to both registered and non-registered users:

- Home
- Product
- Quotation
- Product / Quotation Detail
- Bag

The following pages are open to registered users only:

- Checkout
- Checkout Success
- User Profile

The following user authentication pages are also currently available:

- User Registration
- Sign In
- Sign Out
- Email Verification


### Skeleton

_Desktop Home Page_

![Wireframe](/documentation/screenshots/desktop-wireframe-home.png)

_Desktop Product Page_

![Wireframe](/documentation/screenshots/desktop-wireframe-product.png)

_Desktop Blog Page_

![Wireframe](/documentation/screenshots/desktop-wireframe-blog.png)

_Mobile Product Page_

![Wireframe](/documentation/screenshots/mobile-wireframe-all.png)

__Database Schema__

Database schema.

### Surface Design

The design aims to deliver a website that demonstrates a clear understanding of its purpose.  The overall aesthetic is clean and simple and intends to communicate a professional and friendly organisation.  The Boutique Ado tutorial was used as the starting point for developing the templates for the project.

__Colours__

The website colours were chosen from a furniture image and then applied to the home page and accross the website.

![Furniture Image for Coolors](/documentation/screenshots/kam-idris-_HqHX3LBN18-unsplash.jpg)

![Coolors Palette](/documentation/screenshots/coolors.png)

__Typography__

The font family applied for the hero image overlay text is:

font-family: 'Poppins', sans-serif;

The font family applied for the site is:

font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans","Liberation Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";

__Images__

The furniture images chosen for the website aim to show that there is a highly skilled professional organisation producing quality restored furniture.

## Features

__Navigation Bar__

The navigation bar is present on all pages.  It remains at the top of the page at all times to allow the user to navigate easily around the site.  All visitors both registered and unregistered are presented with the navbar. 

![Navigation Bar](/documentation/screenshots/desktop-navbar.png)

---

Along with being a marketing tool, the company name or logo serves as a home page link.

![Navigation Bar](/documentation/screenshots/company-logo.png)

---

On mobile and mediaum screens the home link is present in the dropdown menu.

![Navigation Bar](/documentation/screenshots/home-link-mobile.png)

---

The user can search the site for a specific product using the search feature on the navbar.

![Navigation Bar](/documentation/screenshots/search.png)

---

The products can be sorted by price (high to low or low to high), or by Name, Source, Crafter, or Source (A-Z or Z-A).

![Navigation Bar](/documentation/screenshots/product-sort.png)

---

The Account dropdown offers the unregistered user an opportunity to register or log in.  

![Navigation Bar](/documentation/screenshots/account-menu-not-registered.png)

---

The registered user can review their profile or logout.  The site administrator can also open the product management menu so that products can be viewed, added, updated or deleted.

![Navigation Bar](/documentation/screenshots/account-menu-registered.png)

---

The user has an opportunity to select the All Products menu and choose products sorted by price (low to high), category (A-Z), crafter (A-Z), or Source (A-Z), or they can simply browse all products.  The products can also be selected from the category menus present on the navbar.

![Navigation Bar](/documentation/screenshots/product-dropdown-menus.png)

---

The delivery banner is currently being used to communicate a free delivery message. 

![Navigation Bar](/documentation/screenshots/free-delivery.png)

---

__Footer__

The footer offers the user an opportunity to communicate with the organisation.  There are social media links to Facebook, Instagram and Pinterest along with information for email and phone communication.  The user can aslo subscribe to the mailing list to receive product offers and a copy of the newsletter.  The subscribe button is emphasised in a bright colour.  Having a mailing list of interested visitors and potential customers is a key part of the marketing strategy.  The footer also shows that the Furniture Restoration Collective is a member of the Design and Crafts Council of Ireland thus showing that the organisation is authentic.

![Footer](/documentation/screenshots/footer.png)

---

__Home Page__

The hero image on the home page shows a restored piece of furniture overlayed with information about the products and restoration services offered.  There are also two call-to-action buttons, one to purchase products online and the second to generate a quote to have a furniture piece restored.  The call-to-action buttons are shown in bright colours to attract attention and to encourage users to click through to their chosen product or service.

![Hero Image](/documentation/screenshots/hero-image.png)

---

The crafters involved in the Furniture Restoration Collective are key to its success and therefore it is important to give the visitor an insight into who they are and what their specialities are.  Their images are shown on the home page alng with a brief summary of their backgrounds.  Where possible any relevant SEO keywords have been included to improve web ranking.

![Crafters](/documentation/screenshots/crafters.png)

---

The home page also shows reviews that have been added by customers.  The site administrator has the ability to activate or deactivate a customer review.

![Reviews](/documentation/screenshots/customer-reviews.png)

---

__User Authentication__

A visitor wishing to register can signup by selecting the Register button from the Account dropdown menu.  A valid email address must be entered on the signup screen.

![Signup](/documentation/screenshots/signup-form.png)

---

The password entered must meet minimum security criteria.

![Signup](/documentation/screenshots/signup-form-password.png)

---

An account verification email message will be sent to the new user to complete the registration.

![Signup](/documentation/screenshots/account-verification-email.png)

---

The user profile view allows the user to add a review, add or update their delivery information, or view their orders to date.

![Signup](/documentation/screenshots/user-profile.png)

---

The review form allows the user to enter free text and then select a crafter from the list.

![Review](/documentation/screenshots/product-review.png)

---

Once the user has finished using the site they can select the Logout option from the Account menu.

![Logout](/documentation/screenshots/signout-confirmation.png)

---

__Products__

When the user clicks on the shop online now button or selects products from the navbar dropdown menus, they are brought to the products page.  Here each product has a product image, name, price, the category it belongs to and the crafter name.  Both the category can be selected to show the products in that category.  Likewise, the crafter can be selected and the products they have restored will be shown.  The user can then click on the product image to view the product detail.

![Review](/documentation/screenshots/products.png)

---

The product detail shows a detailed description of the product, a quantity selection option, and additional information about the crafter.  From here the user can choose to add the product to their bag, keep shopping, or use the navbar or footer options.

![Review](/documentation/screenshots/product-detail.png)

---

__Restoration Quotation__

When the user clicks on the get a quote button they are brought to the quotation page.  Here the user can select the category and subcategory based on the furniture restoration project they have in mind.  They will then receive a quotation for the project and have the option get the quote detail.

![Quotation](/documentation/screenshots/quotation.png)

---

The qotation detail shows further information about the quotation in terms of assumptions, transport details, and timing.  Should the user wish to proceed with the restoration work, they can add the service to their bag.

![Quotation Detail](/documentation/screenshots/quotation-detail.png)

---

__Bag__

The shopping bag detail shows the list of products with product name, image, price, and subtotal (in case there are multiple items selected).  Also, there is a bag total, any delivery charges, and a grand total.  The user at this point can decide to progress to the checkout or continue shipping.

![Shopping Bag](/documentation/screenshots/bag-detail.png)

---

__Checkout__

At the checkout, the user is presented with a summary of the order and a form containing any current known information about the customer.  If the user has an account and is logged in, they will be presented with their account information.  There will be a checkbox that can be unchecked if they do not want any changed information saved to their profile.  If the user does not have an account they will be redirected to the login page where they also have the option to register on the site. 

![Checkout](/documentation/screenshots/checkout-personal-details.png)

---

The user then enters their card details at checkout and can complete the order.   

![Checkout](/documentation/screenshots/checkout-card-details.png)

---

Once the payment has been processed, the success page shows the transaction details. 

![Success](/documentation/screenshots/checkout-success.png)

---

An email with a summary of the order is also sent to the customer.

![Success](/documentation/screenshots/order-confirmation-email.png)

---

### Future Features

The following features will be delivered in future iterations of the project.

- Improved profile user interface including a password reset feature.

- A blog showcasing the work of the crafters and delivering video content of the restoration process.

## Technologies Used

### Languages

- [Python](https://www.python.org/) 3.2 was used to develop the application backend.  The following are the Python modules and packages used in the project:

- asgiref==3.6.0
- boto3==1.26.105
- botocore==1.29.105
- dj-database-url==0.5.0
- Django==3.2
- django-allauth==0.41.0
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- django-storages==1.13.2
- gunicorn==20.1.0
- jmespath==1.0.1
- oauthlib==3.2.2
- Pillow==9.4.0
- psycopg2==2.9.5
- python3-openid==3.2.0
- pytz==2022.7.1
- requests-oauthlib==1.3.1
- s3transfer==0.6.0
- sqlparse==0.4.3
- stripe==5.3.0

- [HTML5](https://html.spec.whatwg.org/multipage/) for front-end development.

- [CSS](https://www.w3.org/Style/CSS/) to style the HTML pages

- [JavaScript](https://www.javascript.com//) no was used to create custom dropdown menus in forms

### Frameworks

- [Django](https://docs.djangoproject.com/en/3.2/) v3.2.16
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) v4.6.2

### Database

- [SQLite](https://www.sqlite.org/index.html) for automated testing locally
- [PostgreSQL](https://www.postgresql.org/) from [ElephantSQL](https://www.elephantsql.com/) for live database

### Other

- [Heroku](https://www.heroku.com/) was used to host the deployed site
- [AWS](https://aws.amazon.com/) is hosting the static and media files
- [Gitpod](https://www.gitpod.io/) VS Code Browser as the IDE/Editor
- [Git](https://git-scm.com/) was used for version control 
- [GitHub](https://github.com/) is the repository for the code
- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service(Jigsaw)](https://jigsaw.w3.org/css-validator/)
- [PEP8](https://www.python.org/dev/peps/pep-0008/) is the standard used to validate Python
- [CI Python Linter](https://pep8ci.herokuapp.com/) tool was used to validate the Python code
- [Coolors](https://coolors.co/) generate the colour palette used on the site
- [Balsamiq](https://balsamiq.com/) for developing the wireframes

## Testing

### Manual Testing
<details><summary>User Story Testing</summary>

__EPIC: Site Landing Page__

User Stories:

As a site visitor, I can access the landing page so that I can understand the purpose of the site and take appropriate actions (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/34" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/34/hovercard">#34</a>

To start testing, complete the following steps:
1. Copy the web address https://furniture-restoration.herokuapp.com/ into the browser address bar

Testing procedure:
1. Open the page for the E-Commerce website of Furniture Restoration Collective

Expected Result: The landing page displays the E-Commerce website for Furniture Restoration Collective

Actual Result: The landing page displays the E-Commerce website for Furniture Restoration Collective

---

__EPIC: User Authentication__

User Stories:

As a site visitor, I can register on the site so that I can access the site services and view my profile (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/1" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/1/hovercard">#1</a>

As a registered user, I can trigger an email confirmation after registration so that I understand that my account is registration is complete (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/2" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/2/hovercard">#2</a>

To start testing, complete the following steps:
1. Got to web address https://furniture-restoration.herokuapp.com/ 
2. Find the Account icon in the top right corner

Testing procedure:
1. Click on the Account icon
2. Click on Register
3. Complete the Sign-Up form by entering an email address, username and password
4. Click on Sign Up
5. Check the email account (entered in the Sign Up) for a message asking to confirm the email address 

![Signup Confirm Email](/documentation/screenshots/confirm-email.png)

6. Click on the link in the Email message and confirm that the email address is the correct one for the account
7. The user is brought to the Sign In page

Expected Result: The user can sign in and open their profile from the Account menu

Actual Result: The user can sign in and open their profile from the Account menu

---

As a registered user, I can log in and logout of my account so that I can access my account information (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/3" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/3/hovercard">#3</a>

Testing procedure:
1. Click on the Account icon
2. Click on Login
3. Enter the username or email address, and password
4. Click on Sign In
5. Click on the Account icon

Expected Result: The Profile option is present on the Account dropdown

Actual Result: The Profile option is present on the Account dropdown

---

As a registered user, I can view my profile so that I can review my purchase history (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/4" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/4/hovercard">#4</a>

Testing procedure:
1. Click on the Account icon
2. Click on Login
3. Enter the username or email address and password
4. Click on Sign In
5. Click on the Account icon
6. Select the Profile option
7. Once the profile opens, find the order history heading on the profile page

Expected Result: Any previous purchases are listed in the order history

Actual Result: Any previous purchases are listed in the order history

![Order List in Profile](/documentation/screenshots/order-history-in-profile.png)

---

__EPIC: Manage Products__

User Stories:

To prepare for testing, complete the following steps:
1. Got to web address https://furniture-restoration.herokuapp.com/admin
2. Login using the administrator account
3. Select Products under the Products app
4. A list of products will be shown

As a shop owner, I can add products so that I can keep my store up to date with available products (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/6" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/6/hovercard">#6</a>

As a shop owner, I can view products so that I can see what is available in my store currently (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/7" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/7/hovercard">#7</a>

Testing procedure:
1. Click on the SKU from the product list


Expected Result: Any previous purchases are listed in the order history

Actual Result: Any previous purchases are listed in the order history

As a shop owner, I can update products so that I can ensure the latest product information is shared with customers (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/8" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/8/hovercard">#8</a>

As a shop owner, I can delete products so that I can ensure the product inventory is up to date (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/9" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/9/hovercard">#9</a>




As a shopper, I can view product details so that I can review the price, and description, understand the background of the product, learn about the craftsperson, and view the product image (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/11" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/11/hovercard">#11</a>

As a shopper, I can view the shopping basket total so that I can see how much I need to pay (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/13" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/13/hovercard">#13</a>


EPIC: Product Search and Sort

User Stories:

- As a shopper, I can search for a product by name or description so that I can find what I need to purchase (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/14" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/14/hovercard">#14</a>

- As a shopper, I can sort products by price and name so that I can find the most appropriately priced product for my needs or find by name (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/15" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/15/hovercard">#15</a>

- As a shopper, I can sort a selected category of product by price and name so that I can find the most appropriately priced product for my needs or find by name for the selected category (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/16" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/16/hovercard">#16</a>

EPIC: Shopping Cart

User Stories:

- As a shopper, I can view items in the shopping cart so that I can view total amount due and a list of items I am purchasing (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/17" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/17/hovercard">#17</a>

- As a shopper, I can enter payment details so that I can checkout as quickly and securely as possible (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/18" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/187/hovercard">#18</a>

- As a shopper, I can view order confirmation so that I can check that I have made the correct purchase (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/19" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/197/hovercard">#19</a>

- As a shopper, I can receive an email to confirm the purchase is complete so that I can I have my own record of the transaction (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/20" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/20/hovercard">#20</a>

EPIC: Quote for Custom Restore

User Stories:

- As a site visitor, I can get a quotation so that I can find out the cost of my restoration project (must-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/35" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/35/hovercard">#35</a>

EPIC: Setup UI to Manage Products

User Stories:

- As a shop owner, I can add products in user interface so that I can easily keep my store up to date with available products (should-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/31" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/31/hovercard">#31</a>

- As a shop owner, I can delete products in user interface so that I can ensure the product inventory is up to date (should-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/32" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/32/hovercard">#32</a>

- As a shop owner, I can view products in User Interface so that I can review the price, and description, understand the background of the product, learn about the craftsperson, and view the product image (should-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/33" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/33/hovercard">#33</a>

- As a shop owner, I can edit products in user interface so that I can easily keep my store up to date with available products (should-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/36" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/36/hovercard">#36</a>

EPIC: Crafter Profiles

User Stories:

- As a shop owner, I can add a crafter profile so that I can record information about the crafter community (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/25" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/25/hovercard">#25</a>

- As a shop owner, I can view a crafter profile so that I can ensure the crafter profile is up to date (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/26" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/26/hovercard">#26</a>

- As a shop owner, I can update a crafter profile so that I can keep the crafter profile up to date (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/27" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/27/hovercard">#27</a>

- As a shop owner, I can delete a crafter profile so that I can remove a crafter profile that is no longer relevant (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/28" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/28/hovercard">#28</a>

EPIC: Product Testimonials

User Stories:

- As a shopper, I can add a product testimonial so that I can give product feedback (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/29" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/29/hovercard">#29</a>

- As a shop owner, I can post a product testimonial so that I can share product feedback (could-have/complete) <a href="https://github.com/teresabowe/furniture-restoration-collective/issues/30" data-hovercard-type="issue" data-hovercard-url="/teresabowe/furniture-restoration-collective/issues/30/hovercard">#30</a>




</details>

<details><summary>Features Testing</summary>

</details>

### Validator Testing

<details><summary>HTML Testing</summary>

Nu Html Checker.

</details>

<details><summary>CSS Testing</summary>

W3C CSS Validator.

</details>

</details>

<details><summary>Python Testing</summary>

The PEP8 standards for Python were checked using CI Python Linter.

</details>

<details><summary>Lighthouse Testing</summary>

- Home Page

</details>

### Bugs and Fixes

## Deployment

<details><summary>Elephant SQL</summary>

- Log in to ElephantSQL.com to access the dashboard
- Click “Create New Instance”, Give the plan a Name, Select the Tiny Turtle (Free) plan, Leave the Tags field blank
- Select “Select Region”, select a datacenter
- Then click “Review”
- Check the details are correct and then click “Create instance”
- Return to the ElephantSQL dashboard and click on the database instance name for this project
- In the URL section, clicking the copy icon will copy the database URL to the clipboard
</details>

<details><summary>Create a new Heroku app</summary>

- Click New to create a new app
- Give the app a name and select the region . When done, click Create app to confirm
- Open the Settings tab
- Add the config var DATABASE_URL, and for the value, copy in the database url from ElephantSQL
</details>

<details><summary>Project preparation in Gitpod</summary>

- In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to the external database. pip3 install dj_database_url==0.5.0 psycopg2
- Update the requirements.txt file with the newly installed packages, pip freeze > requirements.txt
- In the settings.py file, import dj_database_url underneath the import for os

        import os
        import dj_database_url

- Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented 
- out and connect to the new ElephantSQL database instead. 
- Paste in the ElephantSQL database URL in the position indicated

        DATABASES = {
            'default': dj_database_url.parse('your-database-url-here')
        }
 
- In the terminal, run the showmigrations command to confirm the connection to the external database
 
        python3 manage.py showmigrations

- If connected there will be a list of all migrations, but none of them are checked off
- Migrate the database models to the new database

        python3 manage.py migrate

- Load in the fixtures. Please note the order is very important here. Load the categories, subcategories, crafters and sources first, then products, as the products require a category to be set
- Create a superuser for the new database

        python3 manage.py createsuperuser

- Finally, to prevent exposing the database when there is a push to GitHub, delete it from the settings.py. It can be setup up again using an environment variable.  Reconnect to the local sqlite database.

        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
</details>

<details><summary>Confirming the Elephant SQL database</summary>

- On the ElephantSQL page for the database, in the left side navigation, select “BROWSER”
- Click the Table queries button, select auth_user
- When “Execute” is clicked, the newly created superuser details are displayed. This confirms the tables have been created and data can be added to the database
</details>

<details><summary>Deploying to Heroku</summary>

- Add the following if statement to settings.py So the database URL wouldn't end up in version control let's use an if statement in settings.py so that when our app is running on Heroku where the database URL environment variable will be defined we connect to Postgres and otherwise, we connect to SQLite.

        if 'DATABASE_URL' in os.environ:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }

- Next, install gunicorn

        pip3 install gunicorn

- Create a Procfile
- Right click on the app name e.g. furniture-restoration and create a new file called Procfile
- Enter the following details in line 1:

        web: gunicorn furniture_restoration.wsgi:application

- Commit and push the changes to gitpod as normal
- Login to Heroku from the command line
- Enter heroku login -i
- Enter the email address to login to Heroku
- The login in credentials to be entered here my differ. If MFA/2FA is enabled, the account login name and Heroku API key are required.
- If needed get a list of the apps on Heroku by entering "heroku apps" at the command line.
- To initialise remote enter

    heroku git:remote -a <app-name>

- To push to Heroku enter
    
    git push heroku main

- Go to Deploy in the Heroku App
- Choose Github as the deployment method
- Connect to the Github repository
- Set to automatically deploy to Heroku
- Make the following changes in settings.py

        # SECURITY WARNING: keep the secret key used in production secret!
        SECRET_KEY = os.environ.get('SECRET_KEY', '')

        # SECURITY WARNING: don't run with debug turned on in production!
        DEBUG = 'DEVELOPMENT' in os.environ

- Commit and push the changes to gitpod as normal and then check the build status in Heroku overview page.
</details>

<details><summary>Create an AWS Account</summary>

- Go to aws.amazon.com and create a new Amazon account.
- When complete go to the "Console Home" on AWS
- From there select S3 to create an S3 bucket
- Select "Create Bucket" on the top right corner
- Add the name of the application e.g. furniture-restoration
- Select the region closest
- Check on "ACLs enabled"
- Check on "Bucket Owner Preferred"
- Uncheck "Block all public access"
- Check on the ackknowledgement that the bucket will be public
- Go to the bottom of the page and select "Create Bucket"
- Select Properties and go to the bottom of the page and select "Static Website Hosting"
- Enter index.html in the index document field
- Enter error.html in the error document field
- Click "Save Changes"
- Go to permissions and then Bucket Policy
- Click on edit
- Copy the ARN reference at the top of this window
- Then click the Policy Generator on the top right corner
- The Type of Policy is S3 Bucket Policy
- Add a * to the Principal field
- Choose "GetObject" from the Actions field
- Paste in the ARN reference into the ARN field
- Click Add Statement and then Generate Policy
- Copy the policy into the Bucket Policy Editor
- It should look something like this:

        {
            "Version": "2012-10-17",
            "Id": "Policy1680546805871",
            "Statement": [
                {
                    "Sid": "Stmt1680546797613",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::furniture-restoration/*"
                }
            ]
        }

Note that there is a /* added to the Resource key.  This must be added manually before saving the policy.
For the Access control list (ACL) section, click edit and enable List for Everyone (public access).

</details>

<details><summary>Setup an AWS group</summary>

- Select the AWS IAM Access Analyzer for S3
- Click on User Groups in the laft pane
- Select Create Group
- Enter the group name e.g. manage-furniture-restoration
- Under "Attach permissions policies" select "create policy"
- Select the json tab and "import managed policy"
- Choose S3
- The code should be update with the ARN previously used and should look like this when complete:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::furniture-restoration",
                "arn:aws:s3:::furniture-restoration/*"
            ]
        }
    ]
}

- Click next on tags
- Click "Review Policy"
- Add a name and description
- Click "Create Policy"
- Go back to the IAM Create Group page
- Click on the new policy
- Then "Create Group"

</details>

<details><summary>Setup an AWS User</summary>

- Select the AWS IAM Access Analyzer for S3
- Click on Add Users
- Enter the user name e.g. furniture-restoration-staticfiles-user
- Click Next
- Select the group name from the list presented e.g. manage-furniture-restoration
- Then "Create User" 
- To download the access keys, click on the Users tab again and the user
- Click on the Access Credentials tab and then find the "Create Access Key" button
- The access keys can be generated and downloaded from here
</details>

<details><summary>Connect to AWS</summary>

- Run the following from the command line:

        pip install boto3
        pip install django-storages
        pip freeze > requirements.txt

- Add the storages app to the apps in settings.py
- Make the following additions to settings.py (add after MEDIA_ROOT settings) and replacing the bucket name and the region name with the appropriate settings.

        if 'USE_AWS' in os.environ:
            # Bucket Config
            AWS_STORAGE_BUCKET_NAME = 'furniture-restoration'
            AWS_S3_REGION_NAME = 'eu-west-1'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            # Static and media files
            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'

            # Override static and media URLs in production
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

- Go to Heroku.
- Remove DISABLECOLLECTSTATIC frm the config vars
- Add the AWS_ACCESS_KEY_ID and the AWS_SECRET_ACCESS_KEY (previously downloaded from AWS)
- Create a custom_storages.py file in the root of the project on Gitpod
- Add the following code:

        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage

        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION


        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION
	
	
- Commit and Push the changes as normal
- Check the deployment log on Heroku and also the S3 bucket on AWS.  The static files should be located there after the deployment is complete.
- For cache control to improve performance, add the following code at the top of the "if 'USE_AWS' in os.environ:" in settings.py

        # Cache control
            AWS_S3_OBJECT_PARAMETERS = {
                'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                'CacheControl': 'max-age=94608000',
            }
</details>

<details><summary>Copy Static Files to AWS</summary>

- Go to the new S3 bucket and create a new folder called media
- Select Upload
- Go to the location of the images and select the images already used on the website
- Under "Permissions" select "Grant public-read access"
- Click Next to the end
</details>

## Credits

- Retrieve data outside of Ajax functions from [Stackoverflow](<https://stackoverflow.com/questions/65529905/use-data-outside-of-ajax-success-call>).
- Implement a dependent dropdown list from [Simple is Better than Complex](<https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html>).  
- How to edit Commits from [GitHub](<https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message>).
- Create a superuser for Heroku from the command line from [Stackoverflow](<https://stackoverflow.com/questions/68109989/unable-to-login-to-heroku-admin-panel-after-successfully-creating-superuser>).
- Migrate to Heroku from the command line from [Stackoverflow](<https://stackoverflow.com/questions/48083216/django-on-heroku-programmingerror-at-relation-does-not-exist>).  
- Referencing media files in HTML from [Stackoverflow](<https://stackoverflow.com/questions/66483647/how-do-i-reference-a-local-media-file-in-a-django-template>).

### Media

__Images__

- [Yellow Upholstered Fireside Chair](https://unsplash.com/photos/_HqHX3LBN18?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) created by Kam Idris - Unsplash.
- [Set of Four Wooden Bar Stools with Black](https://unsplash.com/photos/xa3zvVw10z8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) created by Kevs - Unsplash.
- [Armchair with Retro Vibes in Peach Velvet](https://unsplash.com/photos/TKFskJy8PQ8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) created by Spacejoy - Unsplash.
- [Round Marble Table with Metal Upholstered Chairs](https://unsplash.com/photos/rhcllVy2zBU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) created by Tabitha Turner - Unsplash.
- [Mahogany Table and Chairs](https://unsplash.com/photos/9v7UJS92HYc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) created by Ryan Riggins - Unsplash.
- [Writing Desk in Walnut](https://www.pexels.com/photo/bedroom-interior-with-bed-and-classic-furniture-7061071/) created by Max Rahubovskiy - Pexels.
- [Windsor Style Side Chair in Dark Wood](https://unsplash.com/photos/mAIVaG4mHj8) created by Rumman Amin - Unsplash.
- [Brown Leather Armchairs](<https://unsplash.com/photos/_1dsChCQ_7w?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>) created by Jan Canty - Unsplash.
- [Quotation Product Detail](https://www.pexels.com/photo/a-woman-doing-woodwork-8447848/) created by Los Muertos Crew - Pexels.
- [Olaf Masterson](https://www.pexels.com/photo/skilled-artisan-cutting-wood-at-table-saw-5710847/) created by Anna Shvets - Pexels.
- [Tina Hayes](https://www.pexels.com/photo/woman-in-black-sweater-sitting-at-table-4621912/) created by cottonbro studio - Pexels.
- [Pat Henry](https://www.pexels.com/photo/focused-craftsman-smoothing-wooden-detail-with-sander-5974330/) created by Ono Kosuki - Pexels.
- [Peter Maher](https://www.pexels.com/photo/woodworker-with-hammer-working-with-wood-5711880/>) created by Anna Shvets - Pexels.
- [Alice Bohan](https://www.pexels.com/photo/handywoman-grinding-a-wood-plank-8447849/) created by Los Muertos Crew - Pexels.

__Icons__
- [User](https://fontawesome.com/v5/icons/user?f=classic&s=solid) created by Font Awesome.
- [Basket](https://fontawesome.com/v6/icons/cart-shopping?f=classic&s=solid) created by Font Awesome.



