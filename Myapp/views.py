from django.shortcuts import render,redirect
# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render 
from .models import Post

def index(request):
    Posts=Post.objects.all()
    return render(request,"index.html",{"posts":Posts})

def BlogDetails(request,slug):
    single_blog = get_object_or_404(index,slug=slug,)
    content={
         'single_blog': single_blog

    }
    return render(request,"BlogDetails.html",content)
