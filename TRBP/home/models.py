from typing import Counter, Tuple
from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices

# Create your models here.
 

class Festivals(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/festival',null=True, blank=True ,)
	description=models.TextField(null=True,blank=True)
	def __str__(self):
		return self.name

class Trips(models.Model):
	trip_name=models.CharField(blank=True, max_length=70)
	overview=models.TextField(blank=True)
	def __str__(self):
		return self.trip_name

class Itinerary(models.Model):
	trip= models.ForeignKey(Trips,on_delete= models.CASCADE)
	day= models.CharField(blank=True,null=True, max_length=50)
	content= models.TextField(null=True,blank=True)

	def __str__(self):
		title = (str(self.trip) + '- ' +str(self.day))
		return title


# class Pros:
# 	content=models.TextField(blank=True,null=True)
# 	trip=models.ForeignKey(Trips,on_delete=models.CASCADE)


# class Cons:
# 	content=models.TextField(blank=True,null=True)
# 	trip=models.ForeignKey(Trips,on_delete=models.CASCADE)
class Booking(models.Model):
	Choices= {
		('Mr.','Mr.'),
		('Mrs.','Mrs.'),
		('Miss.','Miss.'),
	}
	pickup= {
		('Yes','Yes'),
		('No','No'),
	}
	payment= {
		('Credit Card','Credit Card'),
		('Cash','Cash'),
		('Traveller Cheque','Traveller Cheque'),
		('Bank Transfer','Bank Transfer'),
	}
	trip_name= models.CharField(max_length=30,null=True,blank=True)
	salutation=models.CharField(choices=Choices, max_length=20,null=True,default='Mr.')
	full_name=models.CharField(max_length=20,null=False)
	email=models.EmailField( max_length=254)
	postal_address=models.CharField(null=True,blank=True, max_length=50)
	telephone=models.CharField(max_length=20 ,null=True,blank=True)
	country=models.CharField(max_length=20,null=True,blank=True)
	numberofperson=models.IntegerField(null=True,blank=True)
	arival=models.DateField(null=True,blank=True)
	pickup=models.CharField(choices=pickup,max_length=10, default=False,blank=True)
	comments= models.TextField(blank=True,null= True)
	pay=models.CharField(choices=payment,max_length=20, default=False,blank=True)


	def __str__(self):
		return self.full_name



