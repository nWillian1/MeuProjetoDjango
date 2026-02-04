from django.urls import path
from blog.views.post_view import PostViews 

urlpatterns = [
    path('', PostViews.as_view(), name='home'),
]