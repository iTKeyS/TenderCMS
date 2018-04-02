from django.urls import path
from .views import post_detail, post_list, category_detail, search, new_post, post_list_admin, edit_post, delete_post

urlpatterns = [
    path('blog-list/', post_list, name='post_list'),
    path('new_post/', new_post, name='new_post'),
    path('results/', search, name="search"),
    path('blog-detail/<slug:id>/', post_detail, name='post_detail'),
    path('category-detail/<slug:id>/', category_detail, name='category_detail'),
    path('post-list/', post_list_admin, name='post_list_admin'),
    path('edit-post/<slug:id>/', edit_post, name='edit_post'),
    path('delete-post/<slug:id/', delete_post, name='delete_post'),
]
