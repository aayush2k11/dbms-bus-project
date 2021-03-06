from busapp.serializers import *
from django.contrib.auth.models import User
from rest_framework import generics

from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from busapp.models import Bus, BusStop, UniversalRoute, RouteStop, Company


# BusStop Apis
class BusStopList(generics.ListCreateAPIView):
	"""
	Return a list of all the bustops available
	Supports Read of all the BusStops and Create for a new BusStop
	"""
	queryset = BusStop.objects.all()
	serializer_class = BusStopSerializer

class BusStopDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Return each individual BusStop
	Supports Read, Update, Destroy
	"""
	queryset = BusStop.objects.all()
	serializer_class = BusStopSerializer


#universal routes api
class UniversalRouteList(generics.ListCreateAPIView):
	queryset = UniversalRoute.objects.all()
	serializer_class = UniversalRouteSerializer

class UniversalRouteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UniversalRoute.objects.all()
	serializer_class = UniversalRouteSerializer

#routesStops api
class RouteStopList(generics.ListCreateAPIView):
	queryset = RouteStop.objects.all()
	serializer_class = RouteStopSerializer

class RouteStopDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = RouteStop.objects.all()
	serializer_class = RouteStopSerializer

#Base Users api
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


#company api
class CompanyList(generics.ListCreateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

#Bus api
class BusList(generics.ListCreateAPIView):
	queryset = Bus.objects.all()
	serializer_class = BusSerializer

class BusDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bus.objects.all()
	serializer_class = BusSerializer
