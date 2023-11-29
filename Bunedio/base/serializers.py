from rest_framework import serializers
from .models import Post,Topic,Comment

class PostSerial(serializers.ModelSerializer):
    lookup_field = 'post' 
    class Meta:
        model = Post
        fields=("creator","topic","name","body","updated","created",)

class TopicSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields="__all__"

class CommentSerial(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields="__all__"