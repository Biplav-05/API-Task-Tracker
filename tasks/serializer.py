from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    address=serializers.CharField()