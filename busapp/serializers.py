from rest_framework import serializers
from busapp.models import BusStop, UniversalRoute, RouteStop, Company, Bus
from django.contrib.auth.models import User
#serializer class for busstops
class BusStopSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusStop
		fields = ('id', 'name')


#serialize users
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')



#serialize universal routes
class UniversalRouteSerializer(serializers.ModelSerializer):
	route_stops = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="routestop-detail")
	source = serializers.HyperlinkedRelatedField(read_only=True, view_name="busstop-detail")
	destination = serializers.HyperlinkedRelatedField(read_only=True, view_name="busstop-detail")
	class Meta:
		model = UniversalRoute
		fields = ('id', 'source', 'destination', 'route_stops')

#serialize route stops
class RouteStopSerializer(serializers.ModelSerializer):
	route = serializers.HyperlinkedRelatedField( read_only=True, view_name="universal-route-detail")
	bus_stop = serializers.HyperlinkedRelatedField( read_only=True, view_name="busstop-detail")
	class Meta:
		model = RouteStop
		fields = ('id', 'route', 'bus_stop', 'bus_stop_number', 'distance')

class CompanySerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField()
	buses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="bus-detail")
	class Meta:
		model = Company
		fields = ('id', 'user', 'name', 'account_number', 'manager_phone', 'buses')

class BusSerializer(serializers.ModelSerializer):
	"""
	#name of the bus company who owns the bus
	owner = models.ForeignKey(Company, related_name='buses')
	#the universal route number this bus travels on
	route = models.ForeignKey(UniversalRoute, related_name='buses')
	#ticket rate in rupees per kilometer
	rate = models.DecimalField(max_digits=3, decimal_places=2)
	#average speed at which this bus travels, used to calculate time of travel
	speed = models.DecimalField(max_digits=5, decimal_places=2)
	#capacity of the bus to get maximum number of allowed customers
	capacity = models.IntegerField()
	#discounts offered on this bus in percentage
	discount = models.DecimalField(max_digits=4, decimal_places=2)
	"""
	owner = serializers.HyperlinkedRelatedField(view_name="company-detail")
	class Meta:
		model = Bus
		fields = ('owner', 'route', 'rate', 'speed', 'capacity', 'discount')
