<h1 align="center">Foody Family</h1>

<img src="" height="400px"> TBC

**Live Site:**
[Foody Family Repository](put website here!)

**Repository:**
[Foody Family Live Site](https://github.com/SamanthaBooth81/foody-family)

# About

Foody Family is a recipe sharing website where users can view, like and comment on recipes and upload their own recipies to share with other users. This project was set up using a Postgresql database and built using Django. Along with Bootstrap to setup the basic layout and stylling. 

# Table of Contents

[User Experience](#user-experience)

[Features](#features)

[Features to be Implemented](#features-to-be-implemented)

[Wireframes](#wireframes)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Validator Testing](#validator-testing)

[Bugs Found](#bugs-found)

[Deployment](#deployment)

[Credit](#credit)

[Acknowledgments](#Acknowledgments)

# User Experience
## User Stories
### Superuser / Admin
- As a Superuser I can approve and manage the recipies uploaded by community members so that anything unsafe can be removed from the website. 
- As a Superuser I can showcase my favourite recipe on the homepage so that other users can try them out. 
- As a Superuser I can be contacted by all users so I can be made aware of any issues.

### General User
- As a General User I can look through a paginated list of recipes so that I can select a recipe to try out.
- As a General User I can search for a recipe so that I can minimise time searching for what I need. 
- As a General User I can view an entire recipe so that I can learn new dishes.
- As a General User I can contact the site owner so that if there is an issue they will be notified.

### Community User
- As a Community User I can log into my own account so I can manage Username and Password information and delete my account.
- As a Community User I create an account so that I can create, edit, update, and delete my own posts.
- As a Community User I can follow other Community Users so I can find recipes from my favourite chefs.
- As a Community User I can like recipes I have tried so that other users may be encouraged to try them. 
- As a Community User I can save recipes to favourites so that I can easily find them again. 

# Features
- View Recipies
- Create an account
- Upload, edit and remove Recipies
- Like, comment and save recipies


# Features to be Implemented
- Follow other users 
- Search/Filter Options 

# Wireframes
All wireframes were created used [Balsamiq](https://balsamiq.com/)

### Homepage

### Registration, Login, Logout

### Recipe Details

### Manage Account

### Profile

### Add Recipe

### Recipe Management 

# Technologies Used

## Languages Used

[html](https://en.wikipedia.org/wiki/HTML)

[CSS](https://en.wikipedia.org/wiki/CSS)

[Python](https://www.python.org/)

## Frameworks, Libraries and Programmes Used 

[GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repositiry, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project, reducing time spent geting the project setup and prevent re-writing existing code.

[Bootstrap](https://getbootstrap.com/) - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes. 

[Cloudinary](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Rbrand&utm_content=492438439811&utm_term=cloudinary&gclid=Cj0KCQiAt8WOBhDbARIsANQLp96hTerzfFJ_P9lX0tEYEdtM3tSsYB6fhw-x3wQxOO0oc4hXm-A2ZBUaAptIEALw_wcB) - Used to store images online for the recipe posts. 

[Summernote](https://summernote.org/) Used to add a text area field to the admin setup to enable a list of ingredients and method steps.


# Testing

## Functionality 

The project follows the below logic: 

<img src="assets/images/logic_flow_chart.png" height="350px"> 


I have manually tested the projecy by:
- Adding multiple recipes to ensure:
    - The layout works as expected
    - The images displayed correctly, whether uploaded by the user or using the placeholder image instead
    - The recipe details were displaying the correct recipe chosen to be viewed 

# Validator Testing

The code was validated using [PEP8](http://pep8online.com/). No errors were retruned. 

# Bugs Found 

I encountered the following issues whilst builing this project:
- Summernote's text area boxes were not displaying as lists on the webpage. To fix this I added |safe to the code linking to those model fields which removed the tags and displayed them as the lists they are. 
- My registration redirect wasn't redirecting as expected. To fix this I removed the URL from the 'form action' to make this an empty string instead. 
- login error message showing __ all __ and then the message. To fix this I ....................

# Deployment 

This project was deployed using Heroku. Some of the steps in this deployment process are used to get the bare minimum of this project up and running prior to adding functionality. 

See the following steps to deploy below:

1. Login to Heroku and Create a New App.

<img src="assets/images/heroku_deployment_1.png" height="120px"> 

2. Give the App a name, it must be unique, and select a region. 

<img src="assets/images/heroku_deployment_2.png" height="180px"> 

3. Click on 'Create App'. This will take you to a page where you can deploy your project. 

4. Next, click on the 'Resources' tab and search for 'Heroku Postgres' in the Add-ons section to add the Heroku Postgres database to the project. 

5. Click on the 'Settings' tab at the top of the page. The following steps must be completed before deployment.

<img src="assets/images/heroku_deployment_3.png" height="180px"> 

6. Scroll down to Config Vars (also known as Environment Variables) and click 'Reveal Config Vars'. Here the database URL is stored, it is the connection to the database, so this must be copied and stored within env.py file within the same directory as the manage.py file. 

The env.py files is where the projects secret environment variables are stored. This file is then added to a gitnore file so it isn't stored publicly within the projects repository.  

7. Next, the secret key needs to be created within the projects env.py file on GitPod and then added to the Config Vars on Heroku. Once added, go to the settings.py file on GitPod.

8. Within the settings.py file you need to import os, import dj_database_url and then write an if statement to import the env.py file in production to avoid an error. 

9. Then, we need to replace the current insecure secret key with **os.environ.get('SECRET_KEY')**, that we set within the env.py file. 

10. Once the secret key is replaced, scroll down to DATABASES to connect to the Postgres database. Comment out the current code and add the following python doctionary:
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

11. The next step is to connect the project to Cloudinary, which is where the media files will be stored. Log into Cloudinary and copy the API environment variable. This needs to be added to the Config Vars on Heroku and to the projects env.py file, removing the 'CLOUDINARY_URL = ' from the beginning of the copied API link. 

12. Then on Heroku add to the Config Vars, DISABLE_COLLECTSTATIC = 1, as a temporary measure to enable deployment without any static files, this will be removed when it is time to deploy the full project.


13. Back onto GitPod, the cloudinary libraries installed now need to be added to the list of installed apps within the settings.py file - 'cloudinary_storage' and 'cloudinary'

14. Next we need to tell Django to use Cloudinary to store our media and static files. Toward the end of our settings.py  file we can add:

- STATIC_URL = '/static/'
- STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
- STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
- MEDIA_URL = '/media/'
- DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

15. Then we need to tell Django where the templates will be stored. At the top of settings.py, under BASE_DIR (the base directory), add a templates directory and then scroll down to TEMPLATES and add the templates directory variable to 'DIRS': []. 

16. Next, create the three above directories, media, static and templates, on the top level with the manage.py file. 

17. Now add our Heroku host name into allowed hosts in our settings.py file, APP_NAME.herokuapp.com, and then also add 'localhost' so the app can also run locally.

18. Finally, to complete the first deployment set up of the skelleton app, create a Procfile so that Heroku knows how to run the project. Within this file add the following:
web: gunicorn foody_family.wsgi
Web tells Heroku to allow web traffic, whilst gunicorn is the server installed earlier, a web services gateway interface server (wsgi). This is a standard that allows Python services to integrate with web servers.


19. Now, go to the 'Deploy' section on Heroku. Find the 'Deployment Method' section and choose GitHub. Then, connected to the relevant GitHub Repository by searching the repository name and clicking 'Connect'.

<img src="assets/images/heroku_deployment_6.png" height="120px"> 

<img src="assets/images/heroku_deployment_6a.png" width="800px"> 

20. Scroll down to the Automatic and Manual Deploys sections. I have enabled Automatic Deploys as I want my project to automatically redeploy if push any changes back into my repository. I then clicked 'Deploy Branch' in the Manual Deploy section and waited as Heroku installed all dependencies and deployed my code. 

<img src="assets/images/heroku_deployment_7.png" height="180px"> 

21. Once the project is finished deploying, click 'view' to see the newly deployed project. 

# Credit
## Content 

I used the following websites to help with different areas of my project:
### Login, Logout & Registration
- [Django - How to log a user out](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-out), to help get the logout functionality working.
- [Coding Entrepreneurs - Django Logout View](https://www.youtube.com/watch?v=66abhpAxMgQ), to help create the Login functionality. 
- [Denis Ivy - User Registration and Login Authentication](https://www.youtube.com/watch?v=tUqUdu0Sjyc), used to help put together Login, Logout and Registration functionality.
- [Stack Overflow - Django logout not working](https://stackoverflow.com/questions/14021913/django-logout-not-working), to correct my url path for the logout function.
- [Django - form.errors](https://docs.djangoproject.com/en/4.0/ref/forms/api/#django.forms.Form.errors), used to figure out how to use form.errors.
- [Hacker Shack - Login Path](https://www.youtube.com/watch?v=Rz6racFuW_Q), used to help put the url path together for the login page.
- [Stack Overflow - redirect() not redirecting](https://stackoverflow.com/questions/62667374/django-redirect-not-redirecting-appends-the-current-path-name-to-the-domai), to figure out why I wasn't being redirected after registering an account.
- [The Pylot - Create Advanced User Sign Up](https://dev.to/thepylot/create-advanced-user-sign-up-view-in-django-step-by-step-k9m), used to help put together the registration view. 

### Stylling
- [Unsplash - Landing Image](https://unsplash.com/photos/DoUgSMezLp0)
- [Logo Font - Google Fonts](https://fonts.google.com/specimen/Ribeye+Marrow?category=Display&preview.text=Foody%20Family&preview.text_type=custom#standard-styles)
- [Unsplash - Recipe Placeholder Image](https://unsplash.com/photos/ezSFnAFi9hY)
- [Font Awsome Heart Likes Icon](https://fontawesome.com/v5.15/icons/heart?style=solid)
- [CSS object-fit property](https://www.w3schools.com/css/css3_object-fit.asp), used to fit recipe image correctly into the layout.


# Acknowledgments
Thank you to all who encouraged and supported me as I created my first full stack website, espcially to my mentor at The Code Institute for his guidance, patience and encouragement. Also a thank you to Tutor Support at the Code Institute for help with anything I found myself stuck on.  
