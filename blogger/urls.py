from django.contrib import admin
from django.urls import include, path

# from blogger.blog.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blogger.blog.urls", namespace="blog")),
]
