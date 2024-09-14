from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseForbidden

from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.core.paginator import Paginator

def post_detail_template(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all() 

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)  
                comment.author = request.user  
                comment.post = post  
                comment.save() 
                return redirect('post_detail_template', pk=pk)
        else:
            return redirect('login')  
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'form': form, 'comments': comments})

@login_required()
def create_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list_template')
    else:
        form = PostForm()

    return render(request, 'form_create.html', {'form': form})

@login_required
def edit_form(request, pk=None):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user.username:
        return HttpResponseForbidden("Only the author of the post is allowed to edit it")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post) 
        if form.is_valid():
            form.save()
            return redirect("post_detail_template", pk=pk)  
    else:
        form = PostForm(instance=post)  

    return render(request, 'form_edit.html', {"form": form, "post": post})

@login_required
def delete_form(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user.username:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    if request.method == 'POST':  # Confirm deletion
        post.delete()
        return redirect('post_list_template')
    
    return render(request, 'form_delete.html', {'post': post})

def post_list_template(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {"page_obj": page_obj})

def post_detail_template(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {'post': post})