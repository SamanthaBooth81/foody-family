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
- As a Superuser I can manage the recipies uploaded by community members so that anything unsafe can be removed from the website. 
- As a Superuser I can showcase my favourite recipe on the homepage so that other users can try them out. 

### General User
- As a General user I can look through a paginated list of recipes so that I can select a recipe to try out.
- As a General user I can search for a recipe so that I can minimise time searching for what I need. 
- As a General user I can view an entire recipe so that I can learn new dishes.

### Community User
- As a community User I can log into my own account so I can manage Username and Password information.
- As a community User I can post and manage my own recipies so I can create, edit, update, and delete my own posts.
- As a community User I can follow other Community Users so I can find recipies from my favourite chefs.
- As a community User I can like recipies I have tried so that other users may be encouraged to try them. 
- As a community User I can save recipies to favourites so that I can easily find them again. 

# Features
- View Recipies
- Create an account
- Upload Recipies
- Like, comment and save recipies
- Follow Chefs 

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


# Testing

## Functionality 

The project follows the below logic: 

<img src="assets/images/logic_flow_chart.png" height="350px"> 

The user must input each entry of data individually as each item has to be validated using different parameters. Once all data is input the system makes its calculations. These inputs and calculations are then pushed back into the approproate worlsheet. 

I have manually tested the projecy by:
- running through a PEP8 linter
- Intentionally added incorrect data to ensure the code rejects it 
- Tested both in Gitpod and Heroku terminals
- Ensured the data input from the deployed terminal pushes the data back into the worksheet as expected (see images below)

<img src="assets/images/heroku_input.png" height="300px"> 

<img src="assets/images/worksheet_output.png" height="80px"> 

# Validator Testing

The code was validated using [PEP8](http://pep8online.com/). No errors were retruned. 

# Bugs Found 

During testing I found that the date was not in the dd/mm/yy format I thought I had set it as. To fix this I changed the order of the following line of code from "day, month, year" to be "year, month, date":

<ins>my_date = date(int(year), int(month), int(day))</ins>

I also found that some user input errors were terminating the code although I used a while loop. To fix this I identified which lines of code were causing the errors using the Traceback in the terminal. What I found was the code that was causing the break in the loop wasn't within the while loop. To fix this I placed the code in the loop and function began to work as expected.  

Currently, there are no bugs found, however, the below pylint errors were appearing in the Problems tab:

<img src="assets/images/pylint_problems.png" height="150px"> 

I attempted to remove the errors however the variables I have stored globally were not working when moved into the module. Therefore I had to use the global keyword within the following functions:
- lesson_duration_data()
- lesson_location_data
- lesson_attendance_data

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

- [Stack Overflow](https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python) to test user input against the lesson_day list.

- [Stack Overflow](https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python) to help with the while loop when writing the lesson day function. 

- [Stack Overflow](https://stackoverflow.com/questions/5619489/troubleshooting-descriptor-date-requires-a-datetime-datetime-object-but-rec) to aid with ensuring the date can be validated correctly in the lesson_date_data function. 

- [Gspread Documentation](https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value) to find out how to link to a column of data in a spreadsheet.

- [Colorama YouTube Video](https://www.youtube.com/watch?v=u51Zjlnui4Y) to find out how to use Colorama to change the text colour seen by the user in the terminal.

- [Lucid Charts](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-921551090622:kwd-33511936169&km_CPC_Country=20485&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&mkwid=sSyVrRTB8_pcrid_442433236001_pkw_lucidchart_pmt_e_pdv_c_slid__pgrid_55688909257_ptaid_aud-921551090622:kwd-33511936169_&gclid=CjwKCAjwzaSLBhBJEiwAJSRoku05OBdnovMIM5_WGqDOlz1tGneFNADPmA-AHWOA1e24IRtSwq7X3BoC_fkQAvD_BwE) to create the logic flow diagram for the project. 

- [W3Schools](https://www.w3schools.com/python/python_variables_global.asp) to help with using the Global keyword. 

- [Geeks for Geeks](https://www.geeksforgeeks.org/python-dictionary-clear/) to help clear the list of user inputs (that were already pushed into the worksheet) if the user chooses to input more data for another lesson. 

- [Maschituts](https://maschituts.com/2-ways-to-loop-back-to-the-beginning-of-a-program-in-python/) for with the code to start the programme again if the user has more data to input. 

- Method 3 on this [Geeks for Geeks](https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/) article to turn a list of strings into a list of integers.

- [Programiz](https://www.programiz.com/python-programming/methods/list/index) and [Stock Overflow](https://stackoverflow.com/questions/42568565/how-to-index-a-list-based-on-user-input-and-print-the-result) to help with using the index to check a user input.

- [Stack Overflow](https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python) to help with comparing the users answer with a list. 

- [Edureka](https://www.edureka.co/blog/python-list-remove/#pop()) to find out how to remove an item from a list.

- [Slack Overflow](https://stackoverflow.com/questions/33076617/how-to-validate-time-format) to help with working on the lesson_time_data function.


# Acknowledgments
Thank you to all who encouraged and supported me as I created my first game, espcially to my mentor for his guidance and patience and tutor support at The Code Institute who helped when I was stuck. 
