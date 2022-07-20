from multiprocessing import context
from re import template
from unicodedata import name
from django.shortcuts import redirect, render
from .models import Post, Devtool

# Create your views here.
def main(request):
    posts = Post.objects.all()

    context = {
        "posts":posts
    }
    return render(request, template_name="posts/main.html", context=context)

def ideaCreate(request):
    if request.method == "POST":
        title = request.POST["title"]
        req_image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = Devtool.objects.get(name=request.POST["devtool"])

        Post.objects.create(title=title, image=req_image, content=content, interest=interest, devtool=devtool)
        return redirect("/")
    
    devtool = Devtool.objects.all()
    context = {
        'devtool' : devtool
    }
    return render(request, template_name="posts/ideaCreate.html", context=context)

def ideaDetail(request, id):
    post = Post.objects.get(id=id)
    devtool = post.devtool.name
    context = {
        "post":post,
        "devtool":devtool
    }
    return render(request, template_name="posts/ideaDetail.html", context=context)

def ideaDelete(request, id):
    Post.objects.filter(id=id).delete()
    return redirect("/")

def ideaUpdate(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        req_image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = Devtool.objects.get(name=request.POST["devtool"])

        Post.objects.filter(id=id).update(title=title, image=req_image, content=content, interest=interest, devtool=devtool)
        return redirect(f"/post/{id}")
    post = Post.objects.get(id=id)
    devtool = Devtool.objects.all()
    myTool = post.devtool.name
    context = {
        "post":post,
        "devtool":devtool,
        "myTool":myTool
    }
    return render(request, template_name="posts/ideaUpdate.html", context=context)


