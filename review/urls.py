from django.conf.urls import patterns, include, url

from .views import ReviewCreate, ReviewList

urlpatterns = patterns('review.views', 
	url(r'^create/$', ReviewCreate.as_view(), name="review-create"),
	url(r'^list/$', ReviewList.as_view(), name="review-list"),
	)