from django.urls import path
from blog.views import (
    post_list, post_detail, 
    post_detail_template, post_list_template, form,
)

urlpatterns = [
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),

    path("template/<int:pk>/", post_detail_template, name='post_detail_template'),
    path("template/", post_list_template,  name='post_list_template'),
    path('post/new/', form, name='form'),
]