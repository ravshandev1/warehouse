from rest_framework import serializers


class WarehouseSerializer(serializers.Serializer):
    warehouse_id = serializers.IntegerField(source='id')
    material_name = serializers.CharField(source='material.name')
    price = serializers.IntegerField()
