from django.shortcuts import render,get_object_or_404, redirect
from .forms import PostForm, CommentForm

# import model
from .models import PostModel
# Create your views here.
def create(request):
    form        = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance        = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('home')
    template    = 'post/create.html'
    context     = {
        'form':form
    }
    return render(request, template, context)

def delete(request, delete_id):
    PostModel.objects.filter(id=delete_id).delete()
    return redirect('post:my_post')

def update(request, update_id):
    post_update     = PostModel.objects.get(id=update_id)
    data            = {
        'title'     : post_update.title,
        'desc'      : post_update.desc,
    }
    post_form       = PostForm(request.POST or None, initial=data, instance=post_update)
    if post_form.is_valid():
        post_form.save()
        return redirect('post:my_post')
    template    = 'post/create.html'
    context     = {
        'form':post_form
    }
    return render(request, template, context)
def my_post(request):
    obj         = PostModel.objects.filter(author=request.user)
    template    = 'post/my_post.html'
    context     = {
        'obj':obj
    }
    return render(request, template, context)

def detail(request, slugInput):
    obj         = get_object_or_404(PostModel, slug=slugInput)
    comments    = obj.comments.filter(active=True)
    form        = CommentForm(request.POST or None)
    if form.is_valid():
        instance        = form.save(commit=False)
        instance.author = request.user
        instance.post   = obj
        instance.save()
        return redirect('post:detail', slugInput=obj.slug )
    template    = 'post/detail.html'
    context     = {
        'obj':obj,
        'form_comment':form,
        'comment':comments,
    }
    return render(request, template, context)
