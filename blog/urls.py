from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^(?P<id>\d+)/$', views.post_details,name='post_details'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post),


]