# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class emp(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	gender=models.CharField(max_length=6)
	email=models.CharField(max_length=50)
	phone=models.IntegerField()
	credit=models.IntegerField()


	def __str__(self):
		return self.name





class trnf(models.Model):
    cfrom=models.CharField(max_length=30)
    cto=models.CharField(max_length=30)
    credit=models.IntegerField()
    def __str__(self):
        return self.credit
