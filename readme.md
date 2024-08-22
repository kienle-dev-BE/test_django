Menu Project

Overview
This Django project provides functionality for importing menu and element data from CSV files into a PostgreSQL database, creating random menus from this data, and displaying these menus on a webpage. The project is built using Django, with tests written using pytest and pytest-django.

Features
Data Import: Import data from element_master.csv and menu_master.csv into the PostgreSQL database.
Random Menu Generation: Generate 10 random menus, each containing 5 randomly selected elements.
Menu Display: Display the generated menus on a webpage.
Testing: Comprehensive testing using pytest and PostgreSQL.

Prerequisites
Python 3.x
PostgreSQL
Django
pip (Python package installer)
Installation

Clone the repository:
https://github.com/kienle-dev-BE/TestDjango.git

cd menu_project
Install dependencies:

pip install -r requirements.txt
Configure PostgreSQL:

Update menu_project/settings.py with your PostgreSQL database credentials.
python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply migrations:



python manage.py makemigrations
python manage.py migrate
Import CSV data:

Place your element_master.csv and menu_master.csv files in the appropriate directory.

Run the import command:
python manage.py import_data

Generate random menus:
python manage.py create_menus

Run the development server:

python manage.py runserver
Visit http://127.0.0.1:8000/ to view the generated menus.