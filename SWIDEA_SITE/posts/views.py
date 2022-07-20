from multiprocessing import context
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
        # devtool = request.POST["devtool"]
        devtool = Devtool.objects.get(name=request.POST["devtool"])

        Post.objects.create(title=title, image=req_image, content=content, interest=interest, devtool=devtool)
        return redirect("/")
    
    devtool = Devtool.objects.all()
    context = {
        'devtool' : devtool
    }
    return render(request, template_name="posts/ideaCreate.html", context=context)

