from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from userauths.models import Profile
from django.core.paginator import Paginator
from django.urls import resolve
from post.models import Post


def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name
    # Profile.objects.get_or_create(user=request.user)
    
    # posts = Post.objects.filter(user=user).order_by('-posted')

    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted')
    else:
        posts.favourite.all()

# pagination
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)       


    context = {
        
        'posts_paginator':posts_paginator,
    }
    return render(request, 'profile.html', context) 
# Create your views here.
