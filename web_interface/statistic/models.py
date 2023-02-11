from django.db import models
from django.contrib.auth.models import User


class Statistic(models.Model):
	number_of_users = models.IntegerField()
	number_of_templates = models.IntegerField()
	number_of_documents = models.IntegerField()
