from rest_framework import serializers

class WorkSpaceListSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField()
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()
    

class WorkSpaceCreateSerializer(serializers.Serializer):
    name=serializers.CharField()
    description=serializers.CharField(required=False)
    user_id = serializers.IntegerField()
    created_at=serializers.DateTimeField(required=False)
    updated_at=serializers.DateTimeField(required=False)

class WorkSpaceDetailSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField()
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()