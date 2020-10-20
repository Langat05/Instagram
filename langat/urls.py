from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url('', views.home, name='home'),
    url(r'^showprofile/(?P<id>\d+)',views.display_profile,name = 'showprofile'),
 
]