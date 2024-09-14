from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import (
    post_list, post_detail, 
    post_detail_template, post_list_template, 
    create_form, edit_form, delete_form, 
    register, user_profile,
    UserDetailAPIView, UserListCreateAPIView,
)

urlpatterns = [
    path("posts/", post_list_template,  name='post_list'),
    path("posts/<int:pk>/", post_detail_template, name='post_detail'),

    path('posts/create/', create_form, name='create_form'),
    path('posts/edit/<int:pk>/', edit_form, name='edit_form'),
    path('posts/delete/<int:pk>/', delete_form, name='delete_form'),

    path('register/', register, name='register'),
    path('profile/', user_profile, name="profile"),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),

    path("backend/", post_list),
    path("backend/<int:pk>/", post_detail),
]
