from django.conf.urls.defaults import *
from twitter.views import *

url_patterns = patterns('',

	# Main entrance
	(r'^$', twitter_main_page),
)