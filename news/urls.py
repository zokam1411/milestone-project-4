from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
