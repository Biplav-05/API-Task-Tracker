from rest_framework import serializers

class SpaceListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    work_space_id = serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField(required=False)
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()

class SpaceCreateSerializer(serializers.Serializer):
    name=serializers.CharField()
    description=serializers.CharField(required=False, allow_blank=True)
    work_space_id = serializers.IntegerField()
    created_at=serializers.DateTimeField(required=False)
    updated_at=serializers.DateTimeField(required=False)

class SpaceDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    work_space_id = serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField(required=False)
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()

class SpaceUpdateSerializer(serializers.Serializer):
    # id=serializers.IntegerField()
    user_id = serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField(required=False, allow_blank=True)
    created_at=serializers.DateTimeField(required=False)
    updated_at=serializers.DateTimeField(required=False)