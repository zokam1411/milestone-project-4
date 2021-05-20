from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import News

from .forms import NewsForm

# Create your views here.


def news(request):
    """ A view to show all news """

    news = News.objects.all()

    context = {
        'news': news
    }

    return render(request, 'news/news.html', context)


def post_detail(request, post_id):
    """ A view to show individual news """

    post = get_object_or_404(News, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'news/post_detail.html', context)


def add_post(request):
    """ Add a post to news """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only club committee member can do that.')
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
