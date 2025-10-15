from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

def blog_index(request):
    """Post.objects.all()을 이용하면 데이터베이스에 있는 모든 QuerySet(전달받은 모델의 객체 목록)을 가져온다
    해당 객체들을 -created_on을 이용하여 오름차순(최신순)으로 정렬한 뒤, context라는 객체에 저장한다.
    향후 for post in posts: {post.title} 과 같이 사용할 수 있게된다.
    """
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts":posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category.order_by("-created_on"))
    context = {
        "category": category,
        "posts":posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context)