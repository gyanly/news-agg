from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect
import feedparser
from datetime import datetime

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'news/article_list.html',{'articles':articles})

def feed_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feed_list.html',{'feeds':feeds})

def new_feed(request):
    if request.method == "POST":
        form =FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit= False)
            feedData = feedparser.parse(feed.url)
            # set some filed
            feed.title = feedData.feed.title
            feed.save()
            
            
            for entry in feedData.entries:
                article = Article()
                article.title = entry.title
                article.url = entry.link
                article.description = entry.description
                d = datetime(*(entry.published_parsed[0:6]))
                article.publication_date = d.strftime('%Y-%m-%d %H:%M:%S') 
                article.feed = feed
                article.save()  
            
            return redirect('/news/feeds/')
    else:
        form = FeedForm()    
    return render(request, 'news/new_feed.html',{'form':form})

