from django.shortcuts import render
from .models import News


# Create your views here.

def news(request):
    """ A view to show all news """

    news = News.objects.all()

    context = {
        'news': news
    }

    return render(request, 'news/news.html', context)
    
