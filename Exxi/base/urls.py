from django.urls import path,include
from rest_framework import routers
from .views import CommentView,TopicView,PostsOnTopicAPIView,PostAPIView,user_view,topic_view

router = routers.DefaultRouter()

# router.register(r'post-data',PostAPIView)
router.register(r'comment-data',CommentView)
router.register(r'topic-list',TopicView)


urlpatterns = [
    path("api/",include(router.urls)),
    #content url deleted
    # path("api/topic-posts/<tp>/",posts_on_topic,name="topic-post"),
    path("api/post-datas/<pp>/",PostAPIView.as_view(),name="post-datas"),
    path("api/user/<uk>/",user_view,name="user"),
    path("api/topic-posts/<tp>/",PostsOnTopicAPIView.as_view(),name="topic-posts"),
    path("api/topics/",topic_view,name="topics"),  
    path("accounts/", include("django.contrib.auth.urls")),
]


# => particular post content              
# => api/post-datas/id
#includes comment on that post and its datas


#topic name 
# -> api/topic-list/

#topic related posts
# -> api/topic-posts/id
# includes posts related to that topic