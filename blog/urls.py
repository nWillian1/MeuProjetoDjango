from django.urls import path
from blog.views.post_view import PostViews, PostDetail

urlpatterns = [
    path('', PostViews.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]