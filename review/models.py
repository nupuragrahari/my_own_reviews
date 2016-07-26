from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from star_ratings.models import Rating


class Review(models.Model):
	PERSONAL, PROFFESIONAL = range(2)
	REVIEW_TYPE = (
		(PERSONAL, 'Personal'),
		(PROFFESIONAL, 'Proffesional'),
		)
	name = models.CharField('Person name', max_length=200)
	reviewer = models.CharField('Your name', max_length=200)
	review_type = models.IntegerField('Review type', choices=REVIEW_TYPE)
	text = models.TextField('Your impression', max_length=200)
	raitings = GenericRelation(Rating, related_query_name='rates')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
