from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'index.html', {
        'posts': posts
    })

def post(request, id):
    postagem = get_object_or_404(Post, id=id)

    return render(request, 'post.html', {
        'post': postagem
    })