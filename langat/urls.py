from django.conf.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('newprofile/',views.profile,name ='profile'),
    path('showprofile/(?P<id>\d+)',views.display_profile,name = 'showprofile'),
    path('image/$', views.add_image, name='upload_image'),
    path('search/',views.search, name='search'),
    path('explore/', views.explore, name='explore'),
    path('comment/(?P<image_id>\d+)', views.comment, name='comment'),
    path('like/(?P<image_id>\d+)', views.like, name='like'),
    path('follow/(?P<user_id>\d+)', views.follow, name='follow'
 
]