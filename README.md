# Babel Overview

Babel is meant to be a Web App that will allow people share the songs they like the most. This is currently under development, and we have implenmented this trial.

The Web App has been developed using Python and Django as the framework. To run it please download the files, and once they are in your local machine start a virtual enviroment with Python. Once initialized, run the requirements.txt file to get Django in your virtual enviroment and run the server!

This are a list of useful commands:
```shell
# Get the repositoy on your machine
git clone <repo URL>

# Create the virtual enviroment on Windows
py -m venv venv

# Active the Virtual Enviroment
venv\Scripts\activate.bat

# Run the requirements.txt to get Django in your project
pip install -r requirements.txt

# Start the server
python manage.py runserver
```

[Babel Software Demo Video](https://youtu.be/zxJKGFmB888)

# Web Pages

The project has currently two web pages, 'Music List' and 'Add Song'.  

Music List, which is the main page, displays a list of songs the user likes. Songs are retrieved from a database in the Babel project. This page and Add Song page are connected trough links.

Add Song, as the name indicates, is the page where you can add the songs you like the most. Music List dynamically displays the songs added in Add Song page.

# Development Environment

* Visual Studio Code
* Python 3.9.4 64-bit
* Git / GitHub
* Django 3.2
* Python Virtual Enviroment

# Useful Websites

* [Django Official Website](https://docs.djangoproject.com/en/3.0/contents/)
* [Real Python](https://realpython.com/get-started-with-django-1/)
* [Microsoft Docs - Django Course](https://docs.microsoft.com/en-us/learn/paths/django-create-data-driven-websites/)

# Future Work
These are some features and ideas I have in mind to implement in the future:
* Change the overall design and structure of the website
* Add a user functionality 
* Add a share functionality