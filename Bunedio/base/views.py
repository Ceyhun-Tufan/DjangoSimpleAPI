from django.shortcuts import render
from .serializers import CommentSerial,PostSerial,TopicSerial
from .models import Comment,Topic,Post
from rest_framework import viewsets

# Ana Sayfa -> Son Kişilerin yazıları

def home_view(requests):
    contents = Post.objects.all()
    content = {"contents":contents}
    return render(requests,"home.html",content)

# Yazıların sayfas -> yazan kişi ve content

def content_view(requests,ck):
    content = Post.objects.get(id=ck)
    return render(requests,"content_page.html",{"content":content})

# Kişiler -> Kendilerine ait yazılar

def user_view(requests,uk):
    return render(requests,"user_page.html",{})



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