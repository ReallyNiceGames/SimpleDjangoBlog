from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_display(request, slug):
    #return HttpResponse(slug)

    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_display.html', {'post': post})

@login_required(login_url="/users/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            postInstance = form.save(commit=False)
            postInstance.author = request.user
            postInstance.save()
            postInstance.slug
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_create.html', {'form':form})