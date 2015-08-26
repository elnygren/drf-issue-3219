from django.contrib.auth.models import User
from django.db import models

class Startup(models.Model):
	admin= models.OneToOneField(User, related_name='admin_of_startup')
	logo = models.ImageField(upload_to='startup_logos/%Y/%m/%d', blank=True, null=True)
