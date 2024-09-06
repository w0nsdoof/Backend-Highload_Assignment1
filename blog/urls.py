from django.urls import path
from blog.views import (
    post_list, post_detail,
)

urlpatterns = [
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),
]