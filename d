[33mcommit 1b7a00ac2f22157563a53407105be43a96b19445[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m)[m
Author: Askar <w0nsdoof@gmail.com>
Date:   Fri Sep 6 15:01:13 2024 +0500

    4.3 Didn't get 'templates'

[1mdiff --git a/blog/__pycache__/serializers.cpython-311.pyc b/blog/__pycache__/serializers.cpython-311.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..9be2eae[m
Binary files /dev/null and b/blog/__pycache__/serializers.cpython-311.pyc differ
[1mdiff --git a/blog/__pycache__/urls.cpython-311.pyc b/blog/__pycache__/urls.cpython-311.pyc[m
[1mindex 0902bec..d94bfc6 100644[m
Binary files a/blog/__pycache__/urls.cpython-311.pyc and b/blog/__pycache__/urls.cpython-311.pyc differ
[1mdiff --git a/blog/__pycache__/views.cpython-311.pyc b/blog/__pycache__/views.cpython-311.pyc[m
[1mindex cf62d9d..2df1dae 100644[m
Binary files a/blog/__pycache__/views.cpython-311.pyc and b/blog/__pycache__/views.cpython-311.pyc differ
[1mdiff --git a/blog/serializers.py b/blog/serializers.py[m
[1mnew file mode 100644[m
[1mindex 0000000..b79e72a[m
[1m--- /dev/null[m
[1m+++ b/blog/serializers.py[m
[36m@@ -0,0 +1,8 @@[m
[32m+[m[32mfrom rest_framework import serializers[m[41m[m
[32m+[m[32mfrom blog.models import Post[m[41m[m
[32m+[m[41m[m
[32m+[m[32mclass PostSerializer(serializers.ModelSerializer):[m[41m[m
[32m+[m[32m    class Meta:[m[41m[m
[32m+[m[32m        model = Post[m[41m[m
[32m+[m[32m        fields = "__all__"[m[41m[m
[32m+[m[41m    [m
\ No newline at end of file[m
[1mdiff --git a/blog/urls.py b/blog/urls.py[m
[1mindex 01ce3f4..bcc0f24 100644[m
[1m--- a/blog/urls.py[m
[1m+++ b/blog/urls.py[m
[36m@@ -1,6 +1,9 @@[m
 from django.urls import path[m
[31m-from .views import hello_blog[m
[32m+[m[32mfrom blog.views import ([m[41m[m
[32m+[m[32m    post_list, post_detail,[m[41m[m
[32m+[m[32m)[m[41m[m
 [m
 urlpatterns = [[m
[31m-    path('', hello_blog, name='hello_blog'),[m
[32m+[m[32m    path("posts/", post_list),[m[41m[m
[32m+[m[32m    path("posts/<int:pk>/", post_detail),[m[41m[m
 ][m
\ No newline at end of file[m
[1mdiff --git a/blog/views.py b/blog/views.py[m
[1mindex c8c7b91..78b2754 100644[m
[1m--- a/blog/views.py[m
[1m+++ b/blog/views.py[m
[36m@@ -1,4 +1,42 @@[m
[31m-from django.http import HttpResponse[m
[32m+[m[32mfrom rest_framework.decorators import api_view[m[41m[m
[32m+[m[32mfrom rest_framework.response import Response[m[41m[m
[32m+[m[32mfrom rest_framework import status[m[41m[m
 [m
[31m-def hello_blog(request):[m
[31m-    return HttpResponse("Hello, Blog!")[m
[32m+[m[32mfrom blog.models import Post[m[41m[m
[32m+[m[32mfrom blog.serializers import PostSerializer[m[41m[m
[32m+[m[41m[m
[32m+[m[32m@api_view(["GET", "POST"])[m[41m[m
[32m+[m[32mdef post_list(request):[m[41m[m
[32m+[m[32m    if request.method == "GET":[m[41m[m
[32m+[m[32m        posts = Post.objects.all()[m[41m[m
[32m+[m[32m        serializer = PostSerializer(posts, many=True)[m[41m[m
[32m+[m[32m        return Response(serializer.data)[m[41m[m
[32m+[m[32m    elif request.method == "POST":[m[41m[m
[32m+[m[32m        serializer = PostSerializer(data=request.data)[m[41m[m
[32m+[m[32m        if serializer.is_valid():[m[41m[m
[32m+[m[32m            serializer.save()[m[41m[m
[32m+[m[32m            return Response(serializer.data, status=status.HTTP_201_CREATED)[m[41m[m
[32m+[m[32m        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m@api_view(["GET", "PUT", "PATCH", "DELETE"])[m[41m[m
[32m+[m[32mdef post_detail(request, pk=None):[m[41m[m
[32m+[m[32m    try:[m[41m [m
[32m+[m[32m        post = Post.objects.get(id=pk)[m[41m[m
[32m+[m[32m    except Post.DoesNotExist as err:[m[41m[m
[32m+[m[32m        return Response({"error" : str(err)})[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    if request.method == "GET":[m[41m[m
[32m+[m[32m        serializer = PostSerializer(post)[m[41m[m
[32m+[m[32m        return Response(serializer.data)[m[41m[m
[32m+[m[32m    elif request.method in ["PUT", "PATCH"]:[m[41m[m
[32m+[m[32m        partial = (request.method == "PATCH")[m[41m[m
[32m+[m[32m        serializer = PostSerializer(instance=post,data=request.data,partial=partial)[m[41m[m
[32m+[m[32m        if serializer.is_valid():[m[41m[m
[32m+[m[32m            serializer.save()[m[41m[m
[32m+[m[32m            return Response(serializer.data)[m[41m[m
[32m+[m[32m        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)[m[41m[m
[32m+[m[32m    elif request.method == "DELETE":[m[41m[m
[32m+[m[32m        post.delete()[m[41m[m
[32m+[m[32m        return Response({"deleted" : True})[m[41m[m
[41m+[m
[41m+        [m
[1mdiff --git a/db.sqlite3 b/db.sqlite3[m
[1mindex 09b72c7..7ae1ee4 100644[m
Binary files a/db.sqlite3 and b/db.sqlite3 differ
[1mdiff --git a/my_blog/__pycache__/settings.cpython-311.pyc b/my_blog/__pycache__/settings.cpython-311.pyc[m
[1mindex 19f9d1d..451f9ca 100644[m
Binary files a/my_blog/__pycache__/settings.cpython-311.pyc and b/my_blog/__pycache__/settings.cpython-311.pyc differ
[1mdiff --git a/my_blog/settings.py b/my_blog/settings.py[m
[1mindex eff9d7f..77f17ee 100644[m
[1m--- a/my_blog/settings.py[m
[1m+++ b/my_blog/settings.py[m
[36m@@ -38,7 +38,8 @@[m [mINSTALLED_APPS = [[m
     'django.contrib.messages',[m
     'django.contrib.staticfiles',[m
 [m
[31m-    'blog'[m
[32m+[m[32m    'blog',[m[41m[m
[32m+[m[32m    "rest_framework"[m[41m[m
 ][m
 [m
 MIDDLEWARE = [[m
