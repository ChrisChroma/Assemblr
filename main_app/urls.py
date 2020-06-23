from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts_index, name='index'),
    path('posts/<int:post_id>/', views.posts_detail, name='detail'),

    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),

    path('posts/<int:post_id>/add_message/', views.add_message, name='add_message'),

    
    # path('posts/<int:post_id>/message/<int:message_id>/', views.message_details, name="message_details"),
    path('message/<int:pk>/', views.MessageDetail.as_view(), name="message_details"),
    
]
