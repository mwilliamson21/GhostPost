from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.utils import timezone
from GhostPost.model import Post
from GhostPost.forms import PostForm


def index(request):
    html = 'index.html'
    data = Post.objects.all()
    return render(request, html, {'data': data})


def add_post(request):
    html = 'addpost.html'

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                is_boast=data['is_boast'],
                content=data['content'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = PostForm(request.POST)
    return render(request, html, {'form': form})
