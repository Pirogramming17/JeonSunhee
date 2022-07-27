from django.shortcuts import render, redirect
from .models import Post, Reply

# Create your views here.

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def main(request):
    if request.method == "POST":
        content = request.POST.get("content", False)

        Reply.objects.create(content=content)
        return redirect('/')

    posts = Post.objects.all()
    replys = Reply.objects.all()
    context = {
        'posts' : posts,
        'replys' : replys,
    }
    return render(request, 'posts/main.html', context=context)

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    
    post = Post.objects.get(id=post_id)

    if post.like == True:
        post.like = False
    else:
        post.like = True

    post.save()
    
    return JsonResponse({'id' : post_id})

    

