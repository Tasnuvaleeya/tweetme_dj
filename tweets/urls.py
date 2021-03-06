from django.conf.urls import url
# from .views import tweet_detail_view,tweet_list_view
from .views import (TweetCreateView,
                    TweetDetailView,
                    TweetListView)



urlpatterns =[
    # url(r'^$', tweet_list_view,name="list"),
    # url(r'^1/', tweet_detail_view, name="detail"),
    url(r'^$', TweetListView.as_view(), name='list'), #/tweet/
    url(r'^create/$', TweetCreateView.as_view(), name='create'), #/tweet/create/
    # url(r'^create/$',tweet_create_view, name='create'), #/tweet/create/
    # url(r'^(?P<pk>\d+)', tweet_detail_view, name='detail'),
    url(r'^(?P<pk>\d+)', TweetDetailView.as_view(), name='detail'), #/tweet/1/
]