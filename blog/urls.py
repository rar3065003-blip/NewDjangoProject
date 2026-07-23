from django.urls import path

from .apps import BlogConfig
from .views import (
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("view/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("edit/<int:pk>/", BlogUpdateView.as_view(), name="blog_edit"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),
]
