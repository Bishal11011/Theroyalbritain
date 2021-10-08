from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.shortcuts import redirect, render
from django.urls.conf import include

from .models import Booking, Festivals,Itinerary,Trips,Pros,Cons
from.forms import BookingForm

# Create your views here.

def home(request):
	festivals = Festivals.objects.all()
	context={'festivals':festivals}
	return render(request,'home/home.html',context)

def contact(request):
	if request.method=="POST":
		message_name=request.POST['message-name']
		message_email=request.POST['message-email']
		message_phone=request.POST['message-phone']
		message_text=request.POST['message']
		# send an email
		send_mail(
			'Message From ' + message_name,
			'Phone Number:'+message_phone 
			 + ' Message:'+message_text,	
			message_email,
			['info@theroyalbritainpeak.com']

		)
		return render(request,'home/contactus.html',{'message_name':message_name})

	return render(request,'home/contactus.html')

def royal(request):
	return render(request,'home/royal.html')


def dashain(request):
	return render(request,'home/Dashain.html')
def tihar(request):
	return render(request,'home/Tihar.html')
def loshar(request):
	return render(request,'home/Loshar.html')
def chakchakur(request):
	return render(request,'home/Chakchakur.html')


def people(request):
	return render(request,'home/people.html')

def poonhill(request,pk):
	ponhil=Trips.objects.get(pk =pk)
	itenerary= Itinerary.objects.filter(trip_id= ponhil.id)
	pros= Pros.objects.filter(trip_id= ponhil.id)
	cons= Cons.objects.filter(trip_id= ponhil.id)

	print(itenerary)
	if request.method=='POST':
		form=BookingForm(request.POST)
		if form.is_valid():
			form.save()
	form=BookingForm()
	context={
		'form':form,
		'ponhil':ponhil,
		'itenerary':itenerary,
		'pros':pros,
		'cons':cons
	}
	return render(request,'home/poonhill.html',context)


def festivals(request):
	festivals = Festivals.objects.all()
	context={'festivals':festivals,'media_url':settings.MEDIA_URL}
	return render(request,'home/festival.html',context )


def howtoget(request):
	return render(request,'home/howtoget.html')


def gallary(request):
	return render(request,'home/gallary.html')


def disclaimer(request):
	return render(request,'home/disclaimer.html')

def main(request):
	trip = Trips.objects.all()
		
	return {
		"trip": trip
	}
