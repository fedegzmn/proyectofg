from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proyectofg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'post.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^write_post/$', 'post.views.write_post', name='write_new_post'),    
)

