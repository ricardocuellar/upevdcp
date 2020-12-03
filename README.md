# UPEVDCP project

## Instalations

### Virtual Environment
First you need to install de virtual environment in the server using python.
    | python -m venv .env

### Django 
After install the virtual envitonment you need to install Django in your server or Docker image. In the server you need to use: 
    | pip install django -U

### Mysql Client
For install a mysql client in Django you need to use the command: 
    | pip install mysqlclient


## Creating a DataBase

### Creation
You need to create a new DataBase named "upevdcp" for the project. Also you need to configure your database credentials in settings.py is highly recommended use a exclusive database.