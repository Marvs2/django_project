from django.shortcuts import render

posts = [
    {
        'author': 'MarvinV.',
        'title': 'New Sample 1',
        'content': 'First post for python',
        'date_posted' : 'August 19, 2023'
    },
        {
        'author': 'VinmarM.',
        'title': 'New Sample 2',
        'content': 'Second post for python',
        'date_posted' : 'August 20, 2023'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

 

