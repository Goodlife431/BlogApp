from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello, name='hello'),
    # path('greet/', views.greet, name='greet')
    path('home/', home, name='home'),
    path('',nothing, name='nothing'),
    path('post/',greet, name='hello2'),
    path('detail/<int:pk>/', post_detail, name='post_detail'),
    path('', post_list_view.as_view(), name="home"),
    path('new/', post_create_view.as_view(), name='post_new'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('update/<int:pk>', UpdatePost.as_view(), name='update')
]
