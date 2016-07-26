from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Review

class ReviewCreate(CreateView):
    model = Review
    fields = ['name', 'reviewer', 'review_type', 'text']
    success_url = reverse_lazy('review-list')


class ReviewList(ListView):
	model = Review
