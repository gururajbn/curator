from django.db import models
from django.contrib.auth.models import User

# Create your models here.
categories=(
	('Electronics','Electronics'),
	('Fashion','Fashion'),
	('Food','Food'),
	('Travel','Travel')
	)

class products(models.Model):
	name= models.CharField(max_length=50)
	brand= models.CharField(max_length=50)
	price= models.PositiveSmallIntegerField(default=0)
	category= models.CharField(choices=categories,max_length=50)
	description= models.TextField(blank=True,null=True)
	image=models.URLField()
	curated= models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering= ['-name']


class selected(models.Model):
	user= models.ForeignKey(User)
	product= models.ForeignKey(products)
	time= models.DateTimeField(auto_now_add=True,null=True)

	def __unicode__(self):
		return "%s shortlisted %s on %s" % (self.user,self.product,self.time)

	class Meta:
		ordering= ['-time']