

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

<details><summary>Connect to AWS and Copy Static Files</summary>

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


