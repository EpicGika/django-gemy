from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
	list = [
		('Phone','Phone'),
		('Pc', 'Computer')
	]

	name = models.CharField(max_length=50, verbose_name='title')
	content = models.TextField(null=True, blank=True, verbose_name='describtion')
	price = models.DecimalField(max_digits=5, decimal_places=2)
	image = models.ImageField(upload_to='photos/%y/%m/%d')
	active = models.BooleanField(default=True)
	category = models.CharField(max_length=50, null=True, blank=True, choices=list)
	
	def __str__(self):
		return self.name
	

class test(models.Model):
	date = models.DateField()	#To insert the date 
	time = models.TimeField(null=True)  #To insert the time
	date_time = models.DateTimeField(default=datetime.now)  #To insert both of time and date