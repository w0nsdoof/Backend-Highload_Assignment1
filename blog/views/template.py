from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list_template(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {"page_obj": page_obj})

def post_detail_template(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {'post': post})