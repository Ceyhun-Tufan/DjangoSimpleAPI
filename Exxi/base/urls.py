from django.urls import path,include
from rest_framework import routers
from .views import PostView,CommentView,TopicView,content_view,user_view,topic_view,posts_on_topic

router = routers.DefaultRouter()

router.register(r'post-data',PostView)
router.register(r'comment-data',CommentView)
router.register(r'topic-list',TopicView)


urlpatterns = [
    path("api/",include(router.urls)),
    path("api/content/<str:ck>/",content_view,name="content"),
    path("api/user/<uk>/",user_view,name="user"),
    path("api/topic-posts/<tp>/",posts_on_topic,name="topic-post"),
    path("api/topics/",topic_view,name="topics"),  
    path("accounts/", include("django.contrib.auth.urls")),
    # ekstra parametre verildiyse views kısmında da request dışıdna o parametreleri
    # yazmalısın
]