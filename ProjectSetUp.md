# Basic web application developed using Django Python framework

## Installation

The demo web app is developed using django framework 3.0.3 version (Feb,02,2020). Check if the django is installed in your system

```
python -m django --version
```

The above command should output the Django version installed in your system. I used the Django 3.0.3 for this application development. If your system doesn't have Django, you will get an error telling "No module named django".

Use below command for Django installation

```
pip install django
```
To check the Python version installed in your system, use below command:

```
Python --version
```
## Creating a basic project

Assuming you are staring fresh, you will have to auto-generate some code that establishes a Django-project - a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

Go to the directory where you would like to store your code

```
cd path-to-directory
```

Once you are in the directory where you want to store your project code, run following command:

```
django-admin startproject webappname
```