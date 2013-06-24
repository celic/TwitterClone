from django.db import models

class User(models.User):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 75)
	password = models.CharField(max_length = 20)

class Tweet(models.Model):
	message = models.CharField(max_length = 140)