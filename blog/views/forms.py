from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseForbidden

from blog.models import Post
from blog.forms import PostForm


def create_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('post_list_template')
    else:
        form = PostForm()

    return render(request, 'form_create.html', {'form': form})

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

def delete_form(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user.username:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    if request.method == 'POST':  # Confirm deletion
        post.delete()
        return redirect('post_list_template')
    
    return render(request, 'form_delete.html', {'post': post})
