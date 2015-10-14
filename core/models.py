from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.


class Student(models.Model):
	name = models.CharField(max_length=30, null=True, blank=True)
	email = models.EmailField(max_length=100, null=True, blank=True)
	phone = models.CharField(max_length=15, null=True, blank=True)
	address = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name


	def get_absolute_url(self):
		return reverse(viewname="student_detail", args=[self.id])