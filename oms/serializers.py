from rest_framework import serializers

class OrderSerializer(serializers.Serializer):
    symbol = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    qty = serializers.FloatField(required=True)
    side = serializers.CharField(required=True)