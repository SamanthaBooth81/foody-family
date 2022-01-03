<h1 align="center">Foody Family</h1>

<img src="" height="400px"> TBC

**Live Site:**
[Foody Family Repository](put website here!)

**Repository:**
[Foody Family Live Site](https://github.com/SamanthaBooth81/foody-family)

# About

Recipe website where users can find, view and share recipies with the world! ADD MORE DETAIL HERE!

# Table of Contents

[User Experience](#user-experience)

[Features](#features)

[Features to be Implemented](#features-to-be-implemented)

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
- Follow other users 

## Features to be Implemented
- TBC

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


# Testing

## Functionality 

The project follows the below logic: 

<img src="assets/images/logic_flow_chart.png" height="350px"> 


I have manually tested the projecy by:



# Validator Testing

The code was validated using [PEP8](http://pep8online.com/). No errors were retruned. 

# Bugs Found 


# Deployment 

This project was deployed using the Code Institutes mock terminal for Heroku. 

I followed the following steps:
1. Login to Heroku and Create a New App.

<img src="assets/images/heroku_deployment_1.png" height="120px"> 

2. Give the App a name, it must be unique, and select a region. 

<img src="assets/images/heroku_deployment_2.png" height="180px"> 

3. Click on 'Create App'. This will take you to a page where you can deploy your project. 

4. Click on 'Settings' among the tabs at the top of the page. The following sets must be dione before deployment.

<img src="assets/images/heroku_deployment_3.png" height="180px"> 

5. Next, scroll down to Config Vars (also knownas Environment Variables). In order for Heroku to access my spreadsheet it must have access to the contents of the creds.json file. As this file is to be kept secure it cannot be found in my GitHub repository. To enable access securely, sensitive data is stored in a Config Vars. 

<img src="assets/images/heroku_deployment_4.png" height="120px"> 

6. Click 'Reveal Config Vars'. Where it says 'KEY', input CREDS and 'VALUE', input the contents of the creds.json file. Then click 'ADD'. 
I also had to add a second Config Vars of KEY: PORT and VALUE: 8000, to improve compatability with the Code Institute [Template](https://github.com/Code-Institute-Org/python-essentials-template) I am using.

7. Scroll down to Buildpacks. This adds futher required dependencies outside of the requirements.txt file. Click 'Add Buildpack', select 'python' first and then click 'Save Changes'. 
Then, add a second Buildpack, 'nodejs', to handle the mock terminal provided by The Code Institute.

<img src="assets/images/heroku_deployment_5a.png" height="180px"> 

**The order of these Buildpacks is intentional, ensure Python is on top and nodejs underneath. The order can be changed by clicking and dragging.** 

<img src="assets/images/heroku_deployment_5b.png" height="150px"> 

8. Go to the 'Deploy' section using the tabs at the top. Find the 'Deployment Method' section and choose GitHub. Then, I connected to my relevant GitHub Repository by searching the repository name and clicking 'Connect'.

<img src="assets/images/heroku_deployment_6.png" height="120px"> 

<img src="assets/images/heroku_deployment_6a.png" width="800px"> 

9. Scroll down to the Automatic and Manual Deploys sections. I have enabled Automatic Deploys as I want my project to automatically redeploy if push any changes back into my repository. I then clicked 'Deploy Branch' in the Manual Deploy section and waited as Heroku installed all dependencies and deployed my code. 

<img src="assets/images/heroku_deployment_7.png" height="180px"> 

10. Once my code was finished deploying I clicked view, to see my newly deployed project in the terminal. 

<img src="assets/images/heroku_deployment_8.png" height="150px"> 
<img src="assets/images/heroku_deployment_9.png" height="250px"> 

# Credit
## Content 

I used the following websites to help with different areas of my project:


# Acknowledgments
Thank you to all who encouraged and supported me as I created my first game, espcially to my mentor for his guidance and patience and tutor support at The Code Institute who helped when I was stuck. 
