from django.urls import path
from django.conf import settings

from django.urls import re_path

from .views import (
				HomePageView,
				AboutPageView,
				StopPageView)


urlpatterns = [
	path('about/', AboutPageView.as_view(), name='about'),
	path('', HomePageView.as_view(), name='home'),
]

if settings.STOPED:
	urlpatterns = [
	re_path('.*', StopPageView.as_view()),
	]
