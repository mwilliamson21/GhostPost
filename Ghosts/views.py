from django.shortcuts import render, HttpResponseRedirect, reverse
from Ghosts.forms import PostForm
from Ghosts.models import Post


def index(request):
    html = 'index.html'
    posts = Post.objects.all().order_by('-post_date')
    return render(request, html, {'data': posts})


def up_votes(request, id):

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))

        post.up_votes += 1
        post.net_votes += 1
        post.save()
        return HttpResponseRedirect(reverse('homepage'))


def down_votes(request, id):

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))

        post.down_votes += 1
        post.net_votes -= 1
        post.save()
        return HttpResponseRedirect(reverse('homepage'))


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


def boast(request):
    html = 'boasts.html'
    posts = Post.objects.all().filter(is_boast=True).order_by('-post_date')
    return render(request, html, {'data': posts})


def roast(request):
    html = 'roasts.html'
    posts = Post.objects.all().filter(is_boast=False).order_by('-post_date')
    return render(request, html, {'data': posts})


def deletepost(request, id):
    delete = Post.objects.get(id=id)
    delete = deletepost()
    return render(request, {'delete': delete})
