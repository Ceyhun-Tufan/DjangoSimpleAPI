from django.shortcuts import render
from .serializers import CommentSerial, PostSerial, TopicSerial
from .models import Comment, Topic, Post
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# topiclerin sayfası


def topic_view(requests):
    content = Topic.objects.all()
    return JsonResponse({"contents": list(content.values())})


# Yazıların sayfas -> yazan kişi ve content

def content_view(requests, ck):
    content = Post.objects.get(id=ck)
    return Response({"contents": content})

# Kişiler -> Kendilerine ait yazılar


def user_view(requests, uk):
    content = Post.objects.all().filter(creator=uk)
    return JsonResponse({"contents": list(content.values())})


# REST FRAMEWORK
# class PostView(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerial

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerial


class TopicView(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerial

# APIViews


class PostsOnTopicAPIView(APIView):
    def get(self, request, tp, format=None):
        try:
            topic = Topic.objects.get(id=tp)
        except Topic.DoesNotExist:
            return Response({"error": f"Topic with id {tp} does not exist."}, status=status.HTTP_404_NOT_FOUND)

        posts = Post.objects.filter(topic=topic)
        serializer = PostSerial(posts, many=True)
        return Response({"contents": serializer.data}, status=status.HTTP_200_OK)


class PostAPIView(APIView):
    def get(self, request, pp, format=None):
        try:
            post = Post.objects.get(id=pp)
        except Post.DoesNotExist:
            return Response({"error": f"Post with id {pp} does not exist."}, status=status.HTTP_404_NOT_FOUND)

        serializer_post = PostSerial(post, many=False)
        comments = post.comments.all()
        serializer_comment = CommentSerial(comments, many=True)
        data = {
            "post-data": serializer_post.data,
            "comment-data": serializer_comment.data
        }
        # post data is a dict and comment data is a list
        return Response(data, status=status.HTTP_200_OK)
