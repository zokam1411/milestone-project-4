from django.shortcuts import render, get_object_or_404
from .models import News


# Create your views here.

def news(request):
    """ A view to show all news """

    news = News.objects.all()

    context = {
        'news': news
    }

    return render(request, 'news/news.html', context)


def news_detail(request, post_id):
    """ A view to show individual news """

    post = get_object_or_404(News, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'news/news_detail.html', context)
