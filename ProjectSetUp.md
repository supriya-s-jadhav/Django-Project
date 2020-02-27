# Project set up

# System Requirements

1. Python
3. Virtual environment
5. Django: Python web framework

## Pre-requisite

Considering you have Python installed in your system and virtual environment activated, follow below commands to start building web application using Django framework.

#### Get started : Installation and Development


Install Django
```
pip install django
```

Check Django version installed in your system
```
python -m django --version
```

Create a project
```
django-admin startproject mysite
```

Run the development server. cd into the mysite directory, doing ls command should display several files. Look for manage.py file, if you can see the manage.py file than run the following command.
```
python manage.py runserver 8080
```

Run following command to start building your webapp. It will create a directory in your mysite directory.
```
python manage.py startapp Profile
```

Run the following command to create login credentials for admin
It will throw you errors, look at the last error line which says 'OperationalError: no such table: auth_user'. This means that you have not created database for the project that you will use in your web application.
```
python manage.py createsuperuser
```

Run the following migration commands to create the database for the project. It will give you output message 'No changes detected'
```
python manage.py makemigrations
```

Run following command to create the database and add few default tables for your project eg auth_user table etc.
```
python3 manage.py migrate
```

Now run the command to create admin user credentials
```
python3 manage.py createsuperuser
```

Run migrations command in order to get changes in the databases. It will give the output following the command
```
python3 manage.py makemigrations
```
Sample output:
```
Migrations for 'Profile':
  Profile/migrations/0001_initial.py
    - Create model Post
```

Run following command to make migrations up-to-date
```
python3 manage.py migrate
```
Sample output
```
perations to perform:
  Apply all migrations: Profile, admin, auth, contenttypes, sessions
Running migrations:
  Applying Profile.0001_initial... OK
```
Activate shell. Press Ctrl+L (for Mac users) to clear the shell screen

```
python3 manage.py shell
>>> from Profile.models import Post
>>> from django.contrib.auth.models import User
>>> Post.objects.all() #null
>>> User.objects.all()
>>> user = User.objects.filter(username='ShivPriya').first()

# create new post and make user as author of that post
post_1 = Post(title='Blog 1',content='First Post Content!',author=user)
>>> Post.objects.all() #null
>>> post_1.save()
>>> Post.objects.all() #shows object 1
>> exit()

python3 manage.py shell
>>> from Profile.models import Post
>>> from django.contrib.auth.models import User
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>]>
# since we exit from the shell, value of the variable user is gone. Let's create teh user variable again
>>> user = User.objects.filter(username='ShivPriya').first()
# create second blog content
>>> post_2 = Post(title='Blog 2', content='Second Post Content!',author=user)
# REMEMBER to save the content
>>> post_2.save()
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>]>

# to get all the post a user created
>>> user.post_set.all()

# another way to create content and automatically save to the database
>>> user.post_set.create(title='Blog 3',content='Third Post content!')
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>]>

```

# Key get-away

## Where to define website content ?

```
mysite/Profile/views.py
```
Any function defined in this file is the content you want to display on your website pages

## Where to point in the file to display the content on the website pages ?

```
mysite/Profile/urls.py
```
Include the function defined in views.py here in a path function as follows.
```
    path("", views.index, name='index')
```
mysite/mysite/urls.py

This is the place where you will point to the urls.py file in Profile folder which will display the content on server.
```
urlpatterns = [
    path('', include("Profile.urls")),
    path('admin/', admin.site.urls),
]
```