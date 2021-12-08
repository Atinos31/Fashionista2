<h1 align="center"> FASHIONISTA </h1><br>
--------<br>
[VIEW LIVE SITE]()

### About 
This project deals with developing a Virtual website ‘E-commerce Website’ MS4 milestone project for code institute.
It provides the user with a list of the various products available for purchase in the store. For the convenience of online shopping, a shopping cart is provided to the user. After the selection of the goods, it is sent for the order confirmation process. The system is implemented using Python’s web framework Django.

![responsiveimage](Documentation/ResponsiveImage.png)


The scope of the project will be limited to some functions of the e-commerce website. It will display products, customers can select catalogs and select products, and can remove products from their cart specifying the quantity of each item. Selected items will be collected in a cart. At checkout, the item on the card will be presented as an order. Customers can pay for the items in the cart to complete an order. This project has great future scope. The project also provides security with the use of login ID and passwords, so that no unauthorized users can access your account. 



## TABLE OF CONTENTS
 * [User Experience UX](#ux-design)
    * [Bussiness Goals](#goals)
    * [User Stories](#stories)
    * [Design](#design) 
    * [Wireframes](#wireframes)
  * [Features](#features)
    * [Existing features](#existing-features)
    * [Features left to implement](#features-left-to-implement)
  * [Technologies Used in the project](#technologies)
    * [Languages](#languages)
    * [Databases ](#databases)
    * [Libraries and frameworks](#libraries-and-frameworks)
    * [Other technologies](#other-technologies)  
  * [Testing](#testing)
    * [Code validation](#code-validation)
    * [Testing User stories](#testing-user-stories)
    * [Responsiveness and Compatibility](#responsiveness-and-compatibility)
    * [Testing performance](#testing-performance)
    * [Testing accessibility](#testing-accessibility)
    * [known bugs](#known-bugs)
  * [Deployment](#deployment)
    * [Deployment of the site](#deployment-of-the-site)
    * [How to run the code locally](#how-to-run-the-code-locally)
   * [Credits](#credits)
     * [Code](#code)
     * [Content](#content)
     * [Media](#media)
     * [Acknowledgment](#acknowledgments)
     
-  ## User Experience:
  -  ## Bussiness Goals
      * Attractive and accessible website that is responsive on all devices.
      * Products on the website can be easily modified(add,update,delete) by the admin.
      * Users can easily register an account
      * Payments via the website are fully secure.
      * The website is accessible also by non registered users.
      * Hold and secure information from all current and new customers so they may login to place orders.

   - ### User Stories:
   
   - #### As a Shopper:
      1. As a shopper, i want to view a list of products so i can select some to purchase.
      2. As a shopper,  i would like view individual product details so i can identify the price and  product description.
      3. As a shopper , i would like to easily identify deals and offers so i can take advantage and save money shopping.
      4. As a shopper, i would like to the total of my purchases to avoid going over my budget.
      5. As a shopper, i would like to sort through a list of available products.
      6. As a shopper, i would like to sort through a specific category of product.
      7. A a shopper, i would like to search for a product using name or description.
      8. As a shopper, i would like to easily see the results of my search queries.
      9. As a shopper, i would like to easily select the size, quantity and color of product i wish to purchase.
      10. A a shopper,  i would like to be able to view items in my cart to be purchased so i can see the total cost and what i will be receiving.
      11. As a shopper, i would like to easily adjust the quantity of the items in my cart so i can easily make changes to my purchase before checkout.
      12. As a shopper , i would like to easily enter my payment information so i can checkout without hassles.
      13. As a shopper, i would like to  be able to fill in my payment information in a secure and safe way.
      14. As a shopper, i would like to view my order confirmation before checkout to verify that i havent made any mistakes.
      15. As a shopper, i would like to receive an email confirmation after checkout so that i can keep the confirmation of what I've purchased for my records.
      16.  As a shopper, i would like to  products that i like to my wishlist.
      17.  As a shopper, i would like read reviews drom other shoppers about cetrain products that i am interested in.
      18.  As a shopper, i would like to able to write reviews on a product i purchased.

      
   - ### As a site user:
     1. As a site user, i would like to easily register for an account so i can have a personalised account and can access my profile.
     2. As a site user, i would like to easily login and logout to access my personal account info.
     3. As a site user, i would like to easily recover my password incase i forget it so that i can recover access to my account.
     4. As a site user, i would like to receive an email confirmation after registering to be able to verify that registration was successfull.
     5. A site user, i would like to have a personalised user profile so that i can view my order history, order confirmation and save my payment information.
     
   - ### As a Store Owner:
     1. As a store owner , i would like to be able to add new products to the store.
     2. As a store Owner , i would like to be able to edit and update a product from the store.
     3. As a store owner , i would like to be able to delete a product from the store.
     
   ## DESIGN
   ### STRUCTURE
  ### Customer Interface:
     1. Customer shops for a product
     2. Customer changes quantity
     3. The customer adds an item to the cart
     4. Customer views cart
     5. Customer checks out
     6. Customer sends order

  Database schema
  ![multiproduct database](documents/diagrams/database.png)


  * Use-Case diagram for customer
  ![use-case diagram for customer](documents/diagrams/customer1.png)

  ### Admin Interface:
    1. Admin logs in
    2. Admin inserts item
    3. Admin removes item
    4. Admin modifies item

  * ER diagram for admin
  ![ER diagram for customer](documents/diagrams/adminer.png)

  * Use-Case diagram for Admin
  ![use-case diagram for customer](documents/diagrams/adminuc.png)

     
   ## Wireframes
    Wireframes/Database Tables Link - [Wireframes](Documentation/Wireframes/Wireframes.pdf)
   *Design Changes to Wireframes**
   
   
## Features

### Existing Features
* customer registers for an account
* customer signs in and out of site
* Customer shops for a product
* Customer changes quantity
* The customer adds an item to the cart
* Customer views cart
* Customer checks out
* customer deletes item from the shopping cart
* customer updates an items in the shopping cart , delete or change sizes.
* customer selects sizes if the item has size options.
* Customer adds product to a wishlist
* customer can scroll back to the top of the page products-page

### Features Left To Implement
* image variations for a particular item
## Technologies Used

* Django
  * Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. https://www.djangoproject.com/

* SQlite3 
   * SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. https://www.sqlite.org/index.html

* PostgreSQL
  * PostgreSQL is a powerful, open source object-relational database system. https://www.postgresql.org/

* Gitpod
  * Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for the web-app. https://www.gitpod.io/
 
* Github
  * GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently during the development of the web-app. https://github.com/

* Heroku
   * This is a cloud based application platform that allows deployment of an application to the web and connection to the database. https://heroku.com/
  
* AWS S3 
  * Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. https://aws.amazon.com/s3/

* Figma 
   * Figma was used to create use-case diagrams

pdf2png site was used to convert pdf files to png [pdf2png](https://pdf2png.com/)


 * Balsamique
   * Balsamiq was used to create the wireframes https://balsamiq.com/
  
### Front-End Technologies

* HTML 5 
  * The web-app uses HTML5 as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a 
better understanding.

* CSS3 
  * The web-app uses CSS3 for styling of elements within the website. It is linked from the page to the *style.css* file.

* Bootstrap4 
  * The open-source Bootstrap framework has been used to implement the layout of the site. Bootstrap is also utilised 
to accommodate the responsive and mobile first design of the dashboard. https://getbootstrap.com/

* Django-forms-bootstrap   
  * A simple bootstrap filter for Django forms. Extracted from the bootstrap theme.
https://django-bootstrap3.readthedocs.io/en/latest/

* JavaScript 
  * The web-app uses Javascript to provide dynamic interactivity, as it is a full-fledged versatile programming language.
https://www.javascript.com/

* JQuery 
   * The web-app uses jQuery, as it simplifies a lot of complicated tasks from JavaScript, such as AJAX calls and DOM manipulation. 
https://www.jquery.com/jquery-3.4.1

* Google Fonts 
  * The dashboard uses Google fonts to accentuate certain text. https://fonts.google.com/

### Back-End Technologies

* Python 
  * Python emphasises readability, uses English keywords and is highly extensible. The core language itself is quite small, 
and it is easy to learn for brginners. https://www.python.org/  

* Gunicorn
   * Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. The Gunicorn server is broadly compatible with 
various web frameworks, simply implemented, light on server resources, and fairly speedy. https://docs.gunicorn.org/en/stable/

* Pillow
   * The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides
extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. 
https://pillow.readthedocs.io/en/stable/handbook/overview.html

* Psycopg
   * Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are 
the complete implementation of the Python DB API 2.0 specification and the thread safety. https://pypi.org/project/psycopg2/ 

* boto3
   * Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS 
services, such as EC2 and S3. https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

* Jinja 
   * This is a modern and designer-friendly templating language for Python. It is fast, widely used and secure with the optional 
sandboxed template execution environment. https://jinja.palletsprojects.com/en/2.11.x/

* Stripe 
  * Checkout creates a secure, Stripe-hosted payment page that lets you collect payments quickly. It works across devices 
and is designed to increase conversion. Checkout makes it easy to build a first-class payments experience. 
https://stripe.com/docs/payments/checkout

## Testing

### Code validation
* W3C Markup Validation Service for HTML.
* W3C CSS Validation Service was used for validating the code.
* jslint
* http://pep8online.com/ - For Validation Python Code.
* Slack - Peer Code Review Forum.

### Testing User Stories
* users can log in and out of the site
* users can register an acount
*  both unregistered and registered users can browse through all product
* clicking on any individual categories takes us to the specific categories
* users can browse through deals in different categories, women, men and kids.
* users can sort items by price, rating,category and name
* dropdown box updates when a criteria is chosen from the navbar
* search funtionality works and returns the query result searched for

### Responsive and Campartibility Testing

### Testing Performance

### Testing Accessibility

## known bugs
* btt-link hidden not showing once on the bottom of the page - solved with a z-index on btt-button and border color change.
* footer doesnt stick to bottom on empty pages.

## Deployment

### Live Website Link


### Repository Link


### Running Code Locally

To deploy the project the following is required:-

- Github account
- Heroku Account
- AWS Account

To create a clone follow the below steps:- 

Github
1. Login to github and find the repository.
2. Click Code and open with Github Desktop.
3. Follow the prompts in the GitHub Desktop Application.

Heroku Deployment with AWS

1. Install gunicorn, psycopg2-binary and dj-database-url using the PIP Install command.
2. Freeze all the requirements for the project into a requirements.txt file using the pip3 freeze > requirements.txt command.
3. Create a procfile, with the following inside it: web: gunicorn pjc_plant_services_ms4.wsgi:application
4. Push these changes to GitHub, using git add . git commit -m and git push commands.
5. Navigate to [Heroku](https://www.heroku.com/), and login or create an account.
6. Once logged in, click on 'resources'.
7. From the add-ons search bar, add the Heroku Postgres DB, select the free account, and then submit order form to add it to the project.
8. From the app's dashboard, click on 'settings', and then 'reveal config vars' in order to set the necessary configuration variables for the project. 
It should look like this: 

| Key                   | Value                      |
|-----------------------|----------------------------|
| AWS_ACCESS_KEY_ID     | Your AWS Access Key        |
| AWS_SECRET_ACCESS_KEY | Your AWS Secret Access Key |
| DATABASE_URL          | Your Database URL          |
| EMAIL_HOST_PASS       | Your Email Password        |
| EMAIL_HOST_USER       | Your Email Address         |
| SECRET_KEY            | Your Secret Key            |
| STRIPE_PUBLIC_KEY     | Your Stripe Public Key     |
| STRIPE_SECRET_KEY     | Your Stripe Secret Key     |
| STRIPE_WH_SECRET      | Your Stripe WH Key         |
| USE_AWS               | TRUE                       |

9. Back on the main dashboard, click on 'deploy', and then under the 'Deployment' method section, select GitHub and 'Automatic Deploys'.

10. Ensure that in settings.py, the following code is commented out:

Database
 https://docs.djangoproject.com/en/3.1/ref/settings/#databases

and the following code is added:

DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
11. Make migrations using the following command:
python3 manage.py makemigrations
and migrate the database models to the Postgres database using the following command:
python3 manage.py migrate

12. New products can be entered via the Django Admin panel or the SQLLite Database can be imported by using the following command
python3 manage.py loaddata

13. Create a new superuser with the following command:
python3 manage.py createsuperuser
and then enter chosen email, username and password.

14. In settings.py, contain the previously entered database setting in an if statement, and add an else condition, so that different databases are 
used depending on the environment.

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

15. Disable 'COLLECTSTATIC' with the fillowing code: heroku config:set DISABLE_COLLECTSTATIC=1
so that Heroku doesn't attempt to collect the static files.
16. Add ALLOWED_HOSTS = ['pjc-plant-services-ms4.herokuapp.com', 'localhost', '127.0.0.1'] to settings.py.
17. Add Stripe environment variables to settings.py.
18. Push to Heroku using the following command:
    git push heroku master

Amazon Web Services:

All Static and media files for the deployed version of the site are hosted in a Amazon Web Services(AWS) S3 bucket. 
In order to create your own bucket, please follow the instructions on the AWS website 
[Here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

1. In the gitpod terminal, install boto3 and django-storages using the following commands:
   pip3 install boto3 and pip3 install django-storages
2. Freeze the new requirements into the 'requirements.txt' file using the pip3 freeze > requirements.txt command
3. Add 'storages' to INSTALLED_APPS in settings.py.
4. Add the following code to settings.py in order to link the AWS bucket to the website:

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'ms4-pjc-plant-services'
    AWS_S3_REGION_NAME = 'eu-west-2'
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

5. Create a custom_storages.py file in the root level of the project. Inside it, include the locations of the Static Storage and Media Storage.
6. Delete DISABLE_COLLECTSTATIC from the Heroku Config Variables.
7. Finally, push to GitHub, and all changes should be automatically pushed to Heroku too.

Making a Local Clone:
In order to make a local clone of the PJC Plant Services website, enter git clone https://github.com/Atinos31/Fashionista2 into the terminal. 

Next, create an .env.py file in the root directory of the project, and add it to the .gitignore file. 
The following code needs to be added to the .env.py file:

import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"   

Then make sure that the required packages are installed by running the following command: 
pip install -r requirements.txt

Make migrations and then migrate in order to create a database, by running the following commands:
python3 manage.py makemigrations and python3 manage.py migrate.

New products can be entered via the Django Admin panel or the SQLLite Database can be imported by using the following command
python3 manage.py loaddata

Create a superuser with the following command: python3 manage.py createsuperuser and entering your email, username and password.

Run the app by entering the following command:
python3 manage.py runserver

---

## Credits

### Code

I used the following links to help my coding:-
- Code Institue task project for setup and linking to AWS.
- https://stackoverflow.com/ - for various issues when writing queries in Python.
- https://www.w3schools.com/python/default.asp - for extra help and tuition with Python.
- https://miniwebtool.com/django-secret-key-generator/ - for generating the secret key
- https://getbootstrap.com/docs/5.0/getting-started/introduction/ - For help with bootstrap classes
- http://ami.responsivedesign.is/ - For help with how the site looked on different devices
- https://dashboard.stripe.com/test/dashboard - For stripe JS Code for my project and webhooks testing


### Content
   This README.md file is based on the Code Institute template.


### Media



### Acknowledgements

Many Thanks to the below for the help and guidances throughout my project:- 
- My Mentor 
- Code Institues support team for increasing my hand in date and being supportive.
- The peercode channel on slack for feedback on my website. 
- Code Institute and the Boutique-Ado Project
 


   
    
