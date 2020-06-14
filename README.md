# Piano Studio Kft. - Introduction of a Hungarian piano company  
This web page was created for Code Institute's Fullstack Web Developer Course
 - it served as the work submitted for User-Centric Frontend Development assesment,
 - was updated for Code Institute's Interactive Frontend Development assesment,
 - was second updated / basically re-written for Code Institute's Data Centric Development assesment,
 - and now it is again reborn as the final Full Stack Frameworks assesment.

Piano Studio Kft, a Hungarian family owned and operated piano business
 - describes the owners both in words on the landing page and with a gallery using instagram integration
 - services are listed under a separate tab and form part of the main content
 - pianos for sale tab is interactively updated on the admin interface, stores pictures in AWS S3
 - provides a contact form to make it easy for customers to ask their questions
 - as main part of our services available pianos for rent are dinamically listed
 - customers once registered have a profile page with 
   - their pianos rented
   - summary of their balance
   - Stripe integrated payment if their balance shows outstanding amount

## Demo
The latest heroku active demo can be found [here](https://pianostudiofullstack.herokuapp.com/)
The live outdated version of the company's webpage can be found [here](http://www.pianostudio.hu)

## UX
My goal in the design was to have an easy to use yet fresh appearence. 
The red color scheme was chosen to reflect a conservative but elegant image. 
Material Design by Google is used as backbone, a custom css design is applied on top and Bootstrap formatting is applied to forms.

## Technologies
The web application is written in python with JavaScript augmentation where I felt appropriate or was needed (Stripe integration)
I used github for continuous integration, set up an action for running the tests in both Github and Travis CI and deployment to Heroku only takes place once CI tests are successfully run.

A list of technologies used
1. HTML
2. CSS
3. Material Design
4. Material.io
5. Python
6. JavaScript
7. Django
8. Postgres database hosted in Heroku
8. Instagram API
9. Stripe API
10. Travis CI
11. Github and Github Actions
12. AWS S3 Static files storage
13. SMTP integration to 3rd party SMTP server


## Features
This site uses the native features of Material Design, Django user management and admin interface, Django mail service and integrates with Instagram API, AWS S3, Stripe API, SMTP server, Postgres db. 

1. The users are presented with an introduction of the company
2. The users can view services provided by the company
3. The users can view the pianos for sale section
4. The users can view a real time snapshot of pianos that are available for rent 
5. The users can register and have access to their profile page
6. Tha users if renting a piano can have a look at their balance, payments made and piano on rent
7. The users can make a payment if they have outstanding balance on their profile page using Stripe payment
8. The owner can assign pianos to users on the admin interface
9. The owner can upload pianos for both rental and sale tabs on the admin interface
10. The owner can manage the pianos for rent section on the admin interface


### Features Left to Implement
The Instagram API integration will need to be updated to use short term keys instead of the expiring developer key it uses at the moment.

## Testing
Both travis and Github CI will run the automated tests before a new version of the code is deployed. 
Coverage is targeted to be above 90% and is also stored under htmlcov folder in HTML format.
![Django CI](https://github.com/badiattila/FullStackPianoStudio/workflows/Django%20CI/badge.svg)
[![Build Status](https://travis-ci.com/badiattila/FullStackPianoStudio.svg?branch=master)](https://travis-ci.com/badiattila/FullStackPianoStudio)

Manual testing:
A three user + admin database is created in the Heeroku (hosted version) of the app to enable testing.
The hosted version also has pianos for rent and sample pianos for sale uploaded.
The hosted version of the app has pianos assigned to test users to test profile functionality.
    - Username:TestUser1 Pass:TestPass1 Usecase: has profile but no piano rented and no payment made
    - Username:TestUser2 Pass:TestPass2 Usecase: has profile and one piano rented and no payment made with outstanding balance
    - Username:TestUser3 Pass:TestPass3 Usecase: has profile with multiple pianos rented and a large payment made that covers all costs 
    - AdminUsername: AdminUser AdminPassword: AdminPass1 

The renter user story achieved the intended outcome of introducing the service and the dynamic gallery plus the profile.
The buyer user story is satisfied by having the section Pianos to Sell with dynamic gallery of pianos for sale.
The seller user story is satisfied by having the option to upload pianos for sale on the admin interface.
The customer for services user story has the services section with piano tuning and restoration.
The contact form is sending out emails to attila.badi@gmail.com.
The Instagram API makes the gallery dynamic by showing all uploaded media.

Validation on all forms are as needed.
Social media links are tested and work as intended to both facebook and instagram.

This site was tested across multiple browsers (Chrome, Internet Explorer, FireFox) and on mobile devices (iPhone 6 and Huawei P10) to ensure compatibility and responsiveness. 

## Deployment
The code of this site is hosted in github, automated tests are run in Travis and deployment to Heroku is also automated on every commit if tests pass. 

To run locally, you will need the following environment variables defined:
 - SECRET_KEY - valid Django secret key (use https://miniwebtool.com/django-secret-key-generator/ if you need one)
 - AWS_C9_HOSTNAME - a valid C9 hostname if you run the code in C9 (strongly suggested!)
 - AWS_ACCESS_KEY_ID - a valid AWS access key id
 - AWS_SECRET_ACCESS_KEY - a valid AWS access key
 - DATABASE_URL - a valid postgres database URL
 - STRIPE_PUBLISHABLE - use a valid stripe publishable key
 - STRIPE_SECRET - use a valid stripe secret key
 - EMAIL_HOST - valid SMTP email server hostname
 - EMAIL_PORT - suggest to use secure port example 465
 - EMAIL_USE_SSL - suggest to set it to True
 - EMAIL_HOST_USER - a valid username for the SMTP
 - EMAIL_HOST_PASSWORD - a valid SMTP host password 
 - EMAIL_SUBJECT_PREFIX - for example "[Piano Studio WEB] "
 - INSTAGRAM_DEV_TOKEN - a valid instagram dev token to pianostudio's instagram
You will need the components in requirements.txt deployed (pip3 install -r requirements.txt )
You will need the migrations to be run (python3 manage.py migrate)
And to run the application you will have to run the starting command (in my case: python3 ~/environment/manage.py runserver $IP:$PORT)

## Credits

### Content
All content in this site were written by me. 

### Media
Background photos were taken from [Pexels](https://www.pexels.com/), a stock image library.
Pictures used (pianos owned and for sale sections and introduction) are taken by the owners and workers of Piano Studio Kft. 

### Acknowledgements
Code Institute's course material is heavily used as both inspiration and code examples.
Color schemes are inspired by an article found https://www.websitebuilderexpert.com/designing-websites/how-to-choose-color-for-your-website/
Instagram integration uses samlpe code from code institute and Instagrams own introductory how-to manuals.
StackOverflow is used to figure out solutions in all cases I got stuck with anything.
CSS Tutorial was at help whenever I needed a nicer interpretation https://www.w3schools.com/css/
For the parts where I got stuck with django I used 
 - https://learndjango.com/tutorials/
 - https://docs.djangoproject.com/en/3.0/topics/auth/default/
 - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
**This is for educational use and possibly will be the successor of the currently hosted www.pianostudio.hu in the future.** 

