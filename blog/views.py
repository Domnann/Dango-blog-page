from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'authour': 'DomnanG',
        'title': 'Blog Post',
        'content' : 'my first post',
        'date_posted' : 'May 7, 2022'
    },
    {
        'authour': 'Pinkfinger',
        'title': 'Blog Post 2',
        'content' : 'my second post',
        'date_posted' : 'May 7, 2022'  
    }
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about (request):
    return render(request, 'blog/about.html')

