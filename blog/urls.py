from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import (
    post_list, post_detail, 
    post_detail_template, post_list_template, 
    create_form, edit_form, delete_form, 
    register, user_profile,
)


urlpatterns = [
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),

    path("template/", post_list_template,  name='post_list_template'),
    path("template/<int:pk>/", post_detail_template, name='post_detail_template'),

    path('form/create/', create_form, name='create_form'),
    path('form/edit/<int:pk>/', edit_form, name='edit_form'),
    path('form/delete/<int:pk>/', delete_form, name='delete_form'),

    path('register/', register, name='register'),
    path('profile/', user_profile, name="profile"),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

]