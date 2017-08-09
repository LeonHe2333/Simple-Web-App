'''Define URL patterns for learning logs'''

from django.conf.urls import url
from . import views

''' A list of avialable page that can be requested from learning_logs app'''
urlpatterns = [
	# Home Page
	url(r'^$', views.index,name='index'),
	'''
	The r tells Python to interpret the following string as a raw string, 
	and the quotes tell Python where the regular expression begins and ends. 
	The caret (^) tells Python to find the beginning of the string, 
	and the dollar sign tells Python to look for the end of the string. 
	
	In its entirety, this expression tells Python to look for a URL with nothing between the beginning and end of the URL.
	Python ignores the base URL for the project (http://localhost:8000/), 
	so an empty regular expression matches the base URL. 
	Any other URL will not match this expression, 
	and Django will return an error page if the URL requested doesn’t match any existing URL patterns.
	'''
]