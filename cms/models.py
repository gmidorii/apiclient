from django.db import models

# Create your models here.
class Domain(models.Model):
	name = models.CharField('domain', max_length=255)
	ip = models.CharField('IP', max_length=255)

	def __str__(self):
		return self.name

class ConvertParam(models.Model):
	key = models.CharField('key', max_length=255)
	value = models.CharField('value', max_length=255)

	def __str__(self):
		return self.key;
