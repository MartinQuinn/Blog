from django.db import models

# Create your models here.

class Post(models.Model):
	#Title = charfield
	title = models.CharField(max_length = 200)
	#Date
	pub_date = models.DateTimeField()
	#Image
	image = models.ImageField(upload_to='media/')
	#text
	body = models.TextField()
	
	def __str__(self):
		return self.title
		
	#make the date read "Month 00(day) 0000(Year)"
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
		
	#to make a limit of 50 character on the summary
	def summary(self):
		return self.body[:50]