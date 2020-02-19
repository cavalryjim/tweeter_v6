# api/views.py
from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetSerializer
from .permissions import IsTweetAuthorOrReadOnly # new

class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsTweetAuthorOrReadOnly, ] # new
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
