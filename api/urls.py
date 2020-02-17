from django.urls import path
from .views import TweetList, TweetDetail

urlpatterns = [
    path('tweets/', TweetList.as_view()),
    path('tweets/<int:pk>/', TweetDetail.as_view()),
]
