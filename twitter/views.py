from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def twitter_main_page(request):
	return render_to_response('twitter/index.html')