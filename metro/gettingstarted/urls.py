from django.conf.urls import patterns, include, url

from django.conf import settings

from django.conf.urls.static import static

#keep next 2 lines uncommented to enable admin

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'hello.views.home', name='home'),
                       
                       url(r'^db', 'hello.views.db', name='db'),
                       
                       url(r'^home/', 'hello.views.home', name='home'),
                       
                       url(r'^directions/', 'hello.views.directions', name='directions'),
                       
                       url(r'^directions2/', 'hello.views.directions2', name='directions2'),
                       
                       url(r'^info/', 'hello.views.info', name='info'),
                       
                       url(r'^info2/', 'hello.views.info2', name='info2'),
                       
                       url(r'^nearest/', 'hello.views.nearest', name='nearest'),
                       
                       url(r'^nearest2/', 'hello.views.nearest2', name='nearest2'),
                       
                       url(r'^nearest3/', 'hello.views.nearest3', name='nearest3'),
                       
                       url(r'^review/','hello.views.review', name='review'),
                       
                       url(r'^review2/','hello.views.review2', name='review2'),
                       
                       
                       url(r'^review3/','hello.views.review3', name='review3'),
                       
                       
                       url(r'^about/', 'hello.views.about', name='about'),
                       
                       
                       #keep the next 2 lines uncommented to enable admin
                       
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()







