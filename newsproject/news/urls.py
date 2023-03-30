from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list, name='article_list'),
    path('feeds/',views.feed_list, name='feed_list'),
    path('feeds/new',views.new_feed, name='new_feed')
]
