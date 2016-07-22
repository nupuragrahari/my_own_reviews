from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class ProffesionalReview(models.Model):
    name = models.CharField(max_length=200,default='')
    Related_By= models.CharField(max_length=200,default='')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class PersonalReview(models.Model):
    name = models.CharField(max_length=200,default='')
    Related_as = models.CharField(max_length=200,default='')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)