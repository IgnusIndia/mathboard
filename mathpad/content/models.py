from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
	title = models.CharField(max_length=200)


	def __unicode__(self):
		return self.title


class Problem(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=500)

	def __unicode__(self):
		return self.title



class Solution(models.Model):
	answered_by = models.ForeignKey(User)
	question = models.ForeignKey(Problem)
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return self.description
