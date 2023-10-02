from django.db import models



class Person(models.Model):
	username = models.CharField(max_length=30)
	age = models.PositiveSmallIntegerField()
	email = models.EmailField()

	def __str__(self):
		return self.username

