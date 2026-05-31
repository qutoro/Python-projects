from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Article, Comment
from .forms import ArticleForm, CommentForm, EditPostForm,UserForm


def create_post(request):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            pass
    if request.method == 'POST':
        if not user:
            return redirect('register')

        if 'edit_post' in request.POST or 'edit_post_id' in request.POST:
            post_id = request.POST['edit_post_id']
            post = get_object_or_404(Article, id=post_id)
            if user == post.author:
                form = EditPostForm(request.POST, instance=post)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.save()
                    return redirect('chat')


        elif 'add_post' in request.POST:
            form = ArticleForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = user
                post.save()
                return redirect('chat')


        elif 'delete_post' in request.POST or 'delete_post_id' in request.POST:
            post_id = request.POST['delete_post_id']
            post = get_object_or_404(Article, id=post_id)
            if user == post.author:
                post.delete()
                return redirect('chat')


    posts = Article.objects.all().order_by('-date')
    return render(request, 'chat.html', {
        'posts': posts,
        'form': ArticleForm(),
        'edit_form': EditPostForm(),
        'user': user
    })


def comment(request, post_id):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            pass
    post = get_object_or_404(Article, id=post_id)
    if request.method == 'POST':
        if not user:
            return redirect('register')
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.article = post
            new_comment.save()
            return redirect('comment', post_id=post.id)

    comments = Comment.objects.filter(article=post).order_by('-date')
    return render(request, 'comments.html', {'comments': comments, 'user': user, 'post': post, 'form': CommentForm()})
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            return redirect('chat')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})