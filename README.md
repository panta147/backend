# backend
## deploy the django app in pythonanywhere


Step 1: Setup your Django Project (Local Changes)

Let’s create a simple application in Django for showing the deployment. 

    Initialize your Django Project 

django-admin startproject deploy_on_pythonanywhere

    Open project in your editor and under settings.py make:

ALLOWED_HOSTS = ['*']

    Create requirements.txt file using the command

pip3 freeze > requirements.txt



Step 2: Upload Project to GitHub


Step 3: Deploy Project on pythonanywhere

    Create an account on pythonanywhere

    Now click on Console then select Bash 

    Run following commands on bash:
    Clone GitHub repo

    Now create and setup environment variables

    python3 -m venv env #create virtual environment
    source env/bin/activate #activate virtual environment
    cd deploy_on_pythonanywhere #navigate inside your project 
    pip install -r requirements.txt #installing dependencies using requirements.txt

    Now copy the path of your directories which you installed on bash
    Type command on bash

    cd
    ls # get list of directories
    pwd #copy the path for future use


    Now click on Web then select Add a new web app

    Click on next and follow the procedure
    select Django as the framework

    Select python3.8 (latest) and click on next till last.
     

    Now under the Web section open the WSGI configuration file

    Edit WSGI configuration file on line no. 12 and 17 remove the word mysite with your project name which you cloned from GitHub, in my case it is deploy_on_pythonanywhere

    Now it looks like this and then click on save:

    Select Virtualenv section under Web:

    Enter the path of Virtualenv as we created using bash (refer above pwd command for path)

    Click on Reload under the Web section and visit the link
