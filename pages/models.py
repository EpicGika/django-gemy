from django.db import models

# One to one relationship

class Female(models.Model):
	name_female = models.CharField(max_length=50)

	def __str__(self):
		return self.name_female

class Male(models.Model):
	male_name = models.CharField(max_length=50)
	girls = models.OneToOneField(Female, on_delete=models.CASCADE)

	def __str__(self):
		return self.male_name
	

# One to many relationship

class Product(models.Model):
	title = models.CharField(max_length=50)
	def __str__(self):
		return self.title
	
class User(models.Model):
	name = models.CharField(max_length=50)
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

# many to many relationship

class video(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title
	
	
class User_name(models.Model):
	name = models.CharField(max_length=50)
	watch = models.ManyToManyField(video,)

	def __str__(self):
		return self.name