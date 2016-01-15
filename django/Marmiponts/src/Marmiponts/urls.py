from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$','Home.views.home',name='home'),
	url(r'^about/$', 'Home.views.about', name='about'),
	url(r'^contact/$', 'Home.views.contact', name='contact'),

	url(r'^dashboard/$', 'Core.views.dashboard', name='dashboard'),
	url(r'^search/$', 'Core.views.search', name='search'),
	url(r'^personalinfo/$','Core.views.personalinfo', name='personalinfo'),
	url(r'^ingredients/$','Core.views.ingredients', name='ingredients'),
	url(r'^suggest/$','Core.views.suggest', name='suggest'),

	url(r'^forum/$', 'forum.views.forum_dir', name='forum'),
    url(r'^forum/(?P<forum_id>\d+)/$', 'forum.views.thread_dir'),
    url(r'^thread/(?P<thread_id>\d+)/$', 'forum.views.post_dir'),
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
