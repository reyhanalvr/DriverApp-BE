from rest_framework import serializers
from .models import User, Trip, OrderTrip

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role_name = validated_data.pop('role')
        role, created = Role.objects.get_or_create(name=role_name)
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            role=role
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at']
        read_only_fields = ['user', 'status', 'created_at', 'updated_at']

class OrderTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTrip
        fields = ['id', 'trip', 'driver', 'accepted_at']
