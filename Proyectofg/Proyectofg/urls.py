from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('post.urls')), #el conjunto de urls que muestran posts estan en post.urls

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'post.views.login', name='login'),
    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    
    url(r'^write_post/$', 'post.views.write_post', name='write_new_post'),    
)

