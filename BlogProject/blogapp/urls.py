from django import views
from django.urls import path
from blogapp import views

urlpatterns = [
    path("home/",views.home_view),
    path("index/",views.index_view),
    path("register/",views.user_view),
    path("create/",views.create_view),
    path("detail/<int:id>/",views.detail_view),
    path("update/<int:id>/",views.update_view),
    path("delete/<int:id>/",views.delete_view),
    path("user/<int:id>/",views.user_blog_view),
]
