from django.shortcuts import render, get_object_or_404
from slugapp.models import Post

# Create your views here.
def postList(request):
    post = Post.objects.all()
    context = {"post": post}
    return render(request, "post_list.html", context)

def postDetails(request, slug):
     post = get_object_or_404(Post, slug=slug)
     context = {"post": post}
     return render(request, "post_detail.html", context)

