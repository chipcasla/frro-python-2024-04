from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.



def home(request):
    ##Una vez tenemos las entradas recuperadas las pasamos al template mediante el diccionario de contexto:
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': posts})  # editado


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post': post})
