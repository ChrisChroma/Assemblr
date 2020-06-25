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
    path('messages/<int:pk>/update/', views.MessageUpdate.as_view(), name='messages_update'),
    path('messages/<int:pk>/delete/', views.MessageDelete.as_view(), name='messages_delete'),
    path('messages/<int:pk>/', views.MessageDetail.as_view(), name="message_detail"),
    path('accounts/signup/', views.signup, name='signup'),

]
