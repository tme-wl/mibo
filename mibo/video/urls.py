from django.conf.urls import include, url
from django.conf.urls import patterns
from django.contrib import admin
urlpatterns = patterns('video',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^video/', include('video.urls')),
    url(r'^home/','views.home'),
    url(r'^addtag/',"views.addtag"),
)