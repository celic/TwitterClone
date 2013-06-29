from twitterclone.views import *
from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', main_page),

	# Login and Logout
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),

	# Web portal
	(r'^twitter/', include('twitter.urls')),

	# Serve static pages
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root': 'static' }),
)
