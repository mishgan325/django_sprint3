from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/<int:post_id>/',
         views.PostDetailView.as_view(),
         name='post_detail'
         ),
    path('category/<slug:category_slug>/',
         views.CategoryDetailView.as_view(),
         name='category_posts'
         ),
    path('',
         views.IndexListView.as_view(),
         name='index'
         )
]
