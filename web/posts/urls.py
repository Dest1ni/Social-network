from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path('', ShowPosts.as_view(), name = "show-posts"),
    path('create/', CreatePost.as_view(), name = "create-post"),
    path('detail/<int:pk>/', DetailPost.as_view(), name = "detail-post"),
    path('like/', ReactionPostView.as_view(), name = "reaction-post"),
    path('comment/<int:post_id>/', CommentCreateView.as_view(), name = "comment-post"),
    path('comment/like', ReactionCommentView.as_view(), name = "comment-reaction")
]