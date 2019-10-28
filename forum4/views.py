from django.shortcuts import render, redirect
from post.models import PostModel
# import filters dari post
from post.filters import PostFilter

def index(request):
    posts           = PostModel.objects.all()
    posts_filter    = PostFilter(request.POST, queryset=posts)
    template    = 'home.html'
    context     = {
        'post':posts,
        'filter':posts_filter
    }
    return render(request, template, context)