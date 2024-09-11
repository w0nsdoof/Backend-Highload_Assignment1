from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render,redirect, get_object_or_404
from django import http

from blog.models import Post
from blog.serializers import PostSerializer

from .forms import PostForm
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
        return http.HttpResponseForbidden("Only the author of the post is allowed to edit it")

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
        return http.HttpResponseForbidden("You are not allowed to delete this post.")
    
    if request.method == 'POST':  # Confirm deletion
        post.delete()
        return redirect('post_list_template')
    
    return render(request, 'form_delete.html', {'post': post})

def post_list_template(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'post_list': posts})

def post_detail_template(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {'post': post})

@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def post_detail(request, pk=None):
    try: 
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist as err:
        return Response({"error" : str(err)})
    
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method in ["PUT", "PATCH"]:
        partial = (request.method == "PATCH")
        serializer = PostSerializer(instance=post,data=request.data,partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return Response({"deleted" : True})

        
