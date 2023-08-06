django-driverjs
=================
django-driverjs is a wrapper for the [Driver.js](https://github.com/kamranahmedse/driver.js) library.

Installation
------------

Run
``pip install django-driverjs``.  
Once this step is complete add
``"driverjs"`` to your ``INSTALLED_APPS`` setting in your ``settings.py``
file and run ``python manage.py migrate`` to update your database.


Usage
-----
#1 On the django admin panel create a driver and its steps.

#2 Include the static files (provided):

``<script src="{%static 'Driverjs/js/driver.min.js'%}"></script>``

``<link rel="stylesheet" href="{%static 'Driverjs/css/driver.min.css'%}">``

#3 Load the tag and render the javascript:
``{% load driverjs %}``

``{%setup_driver 'your_driver_slug' %}``

#4 Choose a place to start it with:
``[your_driver_slug]_driver.start();``
So if your driver's slug is new_features, a new variable will be declared: ``new_features_driver``

