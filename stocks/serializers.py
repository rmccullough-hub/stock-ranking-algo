from rest_framework import serializers
from .models import Stock, Member

class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stock
		fields ='__all__'

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member
		fields ='__all__'