from django.urls import path,include
from rest_framework import routers
from .views import PostView,CommentView,TopicView,home_view,content_view,user_view

router = routers.DefaultRouter()

router.register(r'post-data',PostView)
router.register(r'comment-data',CommentView)
router.register(r'topic-data',TopicView)


urlpatterns = [
    path("api/",include(router.urls)),
    path("",home_view,name="home"),
    path("content/<str:ck>/",content_view,name="content"),
    path("user/<uk>/",user_view,name="user"),  
    # ekstra parametre verildiyse views kısmında da request dışıdna o parametreleri
    # yazmalısın
]