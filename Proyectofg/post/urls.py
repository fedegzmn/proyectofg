from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(
         r'^post/(?P<idpost>[0-9]+)/$',
         'post.views.one_post', 
         name="one_post"),
    url(
         r'^category/(?P<idcategory>[0-9]+)/$',
         'post.views.posts_by_category',
         name="posts_by_category"),
    url(
         r'^$',
         'post.views.home',
         name='home'),
    url(
        r'^index/',
        'post.views.home',
        name='home'),    
)