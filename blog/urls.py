from django.urls import path
from blog.views import (
    post_list, post_detail, 
    post_detail_template, post_list_template, 
    create_form, edit_form, delete_form,
)

urlpatterns = [
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),

    path("template/", post_list_template,  name='post_list_template'),
    path("template/<int:pk>/", post_detail_template, name='post_detail_template'),

    path('form/create/', create_form, name='create_form'),
    path('form/edit/<int:pk>/', edit_form, name='edit_form'),
    path('form/delete/<int:pk>/', delete_form, name='delete_form'),
]