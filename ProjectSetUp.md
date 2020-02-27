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

examples:
un: admin
pwd: Testadmin123

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
>>> user = User.objects.filter(username='admin').first()

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

## How to do database setup ?

1. Create the table schema in the database

Django comes with built-in admin site where you can work with users and/or groups. By default, the Django ues SQLite database. As a beginner, it's good to experiment with pre-built database.

Run following command to create the tables in the database
```
python3 manage.py migrate
```

2. Create models

Define your models, which is nothing but the database layout. You will register your models in Profile/models.py file using class concepts. You will define as many classes as you want the table schema in your SQLite database. Sample model 'class post' is defined for your reference.

Modify the Profile/models.py file as follows to create a table schema called 'post' in the database with fields Title as Charfield, Content as Textfield, Date posted as DateTimefield and Author as Foreign key.
```
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

3. Install Profile app in mysite project

Modify the mysite/settings.py file as follows to tell the mysite project to include the Profile app.

```
INSTALLED_APPS = [
    'Profile.apps.ProfileConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
4. Activate models

Run the following command to save the changes made in your model and migrate it to the database
```
python3 manage.py makemigrations Profile
```

Run the following command, which takes migration names and returns their SQL
```
python3 manage.py sqlmigrate Profile 0001
```

Run the following command to create those tables in the database
```
python3 manage.py migrate
```

## Three-step guide to make and store the model changes

As you develop your website, your models will change. To save the changes in your database and upgrade your application, remember below three commands

1. Make changes in models in models.py file

2. Run following command to create migrations for those changes
```
python3 manage.py makemigrations
```

3.Run following command to apply those changes to the database
```
python3 manage.py migrate
```