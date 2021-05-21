from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import News, Comment
from .forms import NewsForm, CommentForm

# Create your views here.


def news(request):
    """ A view to show all news """

    news = News.objects.all().order_by('-date_created')

    context = {
        'news': news
    }

    return render(request, 'news/news.html', context)


def post_detail(request, post_id):
    """ A view to show individual news """

    post = get_object_or_404(News, pk=post_id)
    comments = Comment.objects.filter(news=post)

    comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.news = post
            comment.comment_author = request.user
            comment.save()
            messages.success(request, 'Thank you for your comment')
            return redirect(reverse('post_detail', args=[post.id]))
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'comment': comment
    }

    return render(request, 'news/post_detail.html', context)


@login_required
def add_post(request):
    """ Add a post to the news """

    if not request.user.is_superuser:
        messages.error(request, 'Only club committee has access here.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            messages.success(request, 'Post successfully added!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = NewsForm()
        
    template = 'news/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ Edit post in the news """
    if not request.user.is_superuser:
        messages.error(request, 'Only club committee has access here.')
        return redirect(reverse('home'))

    post = get_object_or_404(News, pk=post_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post successfully updated!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = NewsForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'news/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete post from the news page """
    if not request.user.is_superuser:
        messages.error(request, 'Only club committee has access here.')
        return redirect(reverse('home'))
    post = get_object_or_404(News, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('news'))


@login_required
def delete_comment(request, comment_id):
    """ Delete a comment from post """
    if not request.user.is_superuser:
        messages.error(request, 'Only club committee has access here.')
        return redirect(reverse('home'))
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('news'))