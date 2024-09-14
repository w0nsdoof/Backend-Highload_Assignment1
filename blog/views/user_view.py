from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render,redirect
from blog.models import Post

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')  

    posts = Post.objects.filter(author=request.user.id)
    return render(request, 'registration/profile.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list_template')  
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})