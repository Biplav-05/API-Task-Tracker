from rest_framework import serializers

class WorkSpaceListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField(required=False)
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()
    

class WorkSpaceCreateSerializer(serializers.Serializer):
    name=serializers.CharField()
    description=serializers.CharField(required=False, allow_blank=True)
    user_id = serializers.IntegerField()
    created_at=serializers.DateTimeField(required=False)
    updated_at=serializers.DateTimeField(required=False)

class WorkSpaceDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField(required=False)
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()

class WorkSpaceUpdateSerializer(serializers.Serializer):
    # id=serializers.IntegerField()
    user_id = serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField(required=False, allow_blank=True)
    created_at=serializers.DateTimeField(required=False)
    updated_at=serializers.DateTimeField(required=False)