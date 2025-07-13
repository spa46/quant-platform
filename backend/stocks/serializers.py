from rest_framework import serializers
from .models import Index, Ticker, TickerDailyData

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = '__all__'

class TickerDailyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TickerDailyData
        fields = '__all__'
