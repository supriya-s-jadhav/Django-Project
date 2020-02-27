from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime
import re

# Create your views here. Dummy data
posts = [

    {
        'author': 'Supriya J',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Feb 24, 2020'
    },
    {
        'author': 'Shivraj K',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feb 25, 2020'
    }
]
def blog(request):
    context =  {
        'posts': Post.objects.all()
    }
    return render(request, 'Profile/blog.html',context)


def home(request):
    #date_now = datetime.now().strftime ("%A, %d %B, %Y at %X")
    #return HttpResponse("<h1> Home </h1> <br/>Hello, Welcome to my world !! <br/> Its: " + date_now +" <br/> - Shiv")
    return render(request,'Profile/home.html', {'title': 'About'})

def about(request):
    return render(request,'Profile/about.html', {'title': 'About'})




