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

Structure.

### Skeleton

__Wireframes__

Wireframes.

__Database Schema__

Database schema.

### Surface Design

Surface design.

__Colours__

Colours.

__Typography__

Typography.

__Images__

Images.

## Features

__Navigation Bar__

The navigation bar is present on all pages.  It remains at the top of the page at all times to allow the user to navigate easily around the site.  All visitors both registered and unregistered are presented with the navbar. 

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


