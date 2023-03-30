from django.shortcuts import render
from .models import Article, Feed

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'news/article_list.html',{'articles':articles})

def feed_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feed_list.html',{'feeds':feeds})

def new_feed(request):    
    return render(request, 'news/new_feed.html',{})

