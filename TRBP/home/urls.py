from django.urls import path

from . import views


urlpatterns=[
	path('', views.home, name="Home"),
	path('contact/', views.contact, name="contact"),
	path('royal/', views.royal, name="royal"),
	path('dashain/', views.dashain, name="dashain"),
	path('tihar/', views.tihar, name="tihar"),
	path('loshar/', views.loshar, name="loshar"),
	path('poonhill/<int:pk>', views.poonhill, name="poonhill"),
	path('chakchakur/', views.chakchakur, name="chakchakur"),
	path('people/', views.people, name="people"),
	path('howtoget/', views.howtoget, name="howtoget"),
	path('festival/', views.festivals, name="festivals"),
	path('disclaimer/', views.disclaimer, name="disclaimer"),
	path('gallary/', views.gallary, name="gallary"),
]