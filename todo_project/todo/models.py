from django.db import models

# Create your models here

class todo(models.Model):
	title = models.CharField(max_length=255, blank=False)
	completed = models.BooleanField(default=False)

	def __str__(self):
        	#Return a human readable representation of the model instance.
        	return "{} - {}".format(self.title, self.completed)
