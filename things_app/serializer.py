from rest_framework import serializers
from .models import Car

class carsSerializer(serializers.ModelSerializer):
    class Meta:
         model=Car
         fields = '__all__'
         
        #  ['model', 'brand', 'price', 'is_bought', 'buyer_id', 'buy_time']  