from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('upload/', views.upload_photo, name='upload'),
    path('like/<int:photo_id>/', views.like_photo, name='like'),
    path('comment/<int:photo_id>/', views.add_comment, name='comment'),
    path('delete/<int:photo_id>/', views.delete_photo, name='delete'),
]