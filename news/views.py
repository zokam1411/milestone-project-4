from django.shortcuts import render

# Create your views here.

def news(request):
    """ A view to return news page """

    return render(request, 'news/news.html')