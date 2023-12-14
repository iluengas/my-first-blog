from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone


# Create your views here.
def post_list(request):
    posts = Post.objects.all() # grabs every post in database
    return render(request, 'blog/post_list.html', {'posts': posts}) # renders list of post


def post_detail(request, pk):
    post = Post.objects.post = get_object_or_404(Post, pk=pk) # gets post based on key
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        # construct the PostForm with data from the form
        form = PostForm(request.POST)
        if form.is_valid():  # all required fields are valid, text and title
            # do not save the Post model yet by setting commit = False
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
