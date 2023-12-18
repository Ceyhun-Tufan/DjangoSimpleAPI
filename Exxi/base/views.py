from django.shortcuts import render
from .serializers import CommentSerial,PostSerial,TopicSerial
from .models import Comment,Topic,Post
from rest_framework import viewsets
from django.http import JsonResponse

# topiclerin sayfası

def topic_view(requests):
    content = Topic.objects.all()
    return JsonResponse({"contents":list(content.values())})

def posts_on_topic(requests,tp):
    topic = Topic.objects.get(id=tp)
    content = Post.objects.all().filter(topic=topic)
    return JsonResponse({"contents":list(content.values())})

# Yazıların sayfas -> yazan kişi ve content

def content_view(requests,ck):
    content = Post.objects.get(id=ck)
    return JsonResponse({"contents":list(content)})

# Kişiler -> Kendilerine ait yazılar

def user_view(requests,uk):
    content = Post.objects.all().filter(creator=uk)
    return JsonResponse({"contents":list(content.values())})


# REST FRAMEWORK
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerial
        
class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerial

class TopicView(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerial


