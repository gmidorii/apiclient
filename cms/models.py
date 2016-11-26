from django.db import models

# Create your models here.
class Domain(models.Model):
	name = models.CharField('domain', max_length=255)
	ip = models.CharField('IP', max_length=255)

	def __str__(self):
		return self.name
