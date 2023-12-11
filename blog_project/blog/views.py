# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from .forms import PostForm, CommentForm, RatingForm
from django.db.models import Avg

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_param = request.GET.get('next')
            if next_param:
                return redirect(next_param)
            else:
                return redirect(reverse('post_list'))
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'registration/login.html')

def search(request):
    query = request.GET.get('q', '')
    print(f"Search query: {query}")
    if query:
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'blog/search.html', {'results': posts})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'user': request.user, 'object_list': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'user': request.user, 'object': post})

@login_required
def post_create(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Use the correct name here

    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'object': post})

def other_view(request):
    # Your other view logic here
    return render(request, 'blog/other_template.html')

def add_rating(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            rating = Rating.objects.create(user=request.user, post=post, value=value)
            rating.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = RatingForm()

    print(form)  # Add this line to print the form in the console

    return render(request, 'blog/add_rating.html', {'post': post, 'form': form})