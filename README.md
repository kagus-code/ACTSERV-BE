#  ACTSERV Api 

#### This an API endpoint for passwordless authentication,  09/06/2021

#### By **Eston Kagwima**

## Description
This end point connencts to a react front end to enable a user to login without using a password instead a token is sent to them in their email or mobile number depending on the one they choose to log in with. Upon registration a user is also sent a confirmation email to verify their email address
This project was generated with [Django](https://docs.djangoproject.com/en/3.2/) version 3.2.7


### User stories Specification
- When a user enters their email or phone number Django should detect if a user exists or not.

- If the user exists with that email it sends them both an OTP and a magic link with the URL having both a OTP and the user email;

- For an existing user, after the user enters their email or phone number, it should redirect them to enter the OTP;

- For a new user, it should prompt the user to confirm their new account creation details then send out the same, OTP for phone number registration and both OTP and magic link for an email account registration;

- For users using their phone number it sends only the OTP.


- It uses the sent back credentials either OTP or URL to create JWT which will be used  to authenticate the user. The magic link  automatically logs in the user.

 - Twillio account is usedfor sending out the SMS OTP.



## Setup/Installation Requirements
- install Python3.9
- Clone this repository `https://github.com/kagus-code/ACTSERV-BE.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
####  Create the Database
    - psql
    - CREATE DATABASE <name>;
####  .env file
Create .env file and paste paste the following and fill  required fields:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<name>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
    DB_HOST='127.0.0.1'
    MODE='dev'
    ALLOWED_HOSTS='*'
    DISABLE_COLLECTSTATIC=1

    EMAIL_USE_TLS=True
    EMAIL_HOST=''
    EMAIL_HOST_USER=''
    EMAIL_HOST_PASSWORD=''
    EMAIL_PORT=587

    TWILIO_ACCOUNT_SID=''
    TWILIO_AUTH_TOKEN=''

#### Run initial Migration
    python3.9 manage.py makemigrations <name of the app>
    python3.9 manage.py migrate
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000
    Access the different api endpoints by editing the url


## Technologies Used

- Django version 3.2.7
- Python
- Postgressql
- Django Restful api

## link to live site on heroku

## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima
