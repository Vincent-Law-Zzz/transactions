# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	user_name = models.CharField(primary_key=True,max_length=30)
	value = models.FloatField()

	def __str__(self) :
		return self.user_name