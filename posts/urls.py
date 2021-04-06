from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list_and_create, name='main_page'),
    path('data/<int:num_posts>/', views.load_post_data_view, name='load_post_data'),
    path('like-unlike/', views.like_unlike_post, name='like_unlike_post'),
    path('upload/', views.image_upload_view, name='image_upload_view'),
    path('<pk>/', views.post_detail, name='post_detail'),
    path('<pk>/data/', views.post_detail_data_view, name='post_detail_data_view'),
    path('<pk>/update/', views.update_post, name='update_post'),
    path('<pk>/delete/', views.delete_post, name='delete_post'),
]
