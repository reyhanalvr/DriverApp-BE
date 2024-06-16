from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Role, Trip, OrderTrip
from .serializers import UserSerializer, TripSerializer, OrderTripSerializer

class RegisterView(generics.CreateAPIView):
    """
    post:
    Register a new user.
    Request body example:
    {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "password123",
        "phone_number": "1234567890",
        "role": "Driver"
    }
    Response example:
    {
        "id": 1,
        "username": "johndoe",
        "email": "johndoe@example.com",
        "phone_number": "1234567890",
        "role": "Driver"
    }
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    post:
    Obtain JWT token pair (access and refresh tokens).
    Request body example:
    {
        "username": "johndoe",
        "password": "password123"
    }
    Response example:
    {
        "refresh": "refresh-token-here",
        "access": "access-token-here"
    }
    """
    permission_classes = [permissions.AllowAny]

class CreateTripView(generics.CreateAPIView):
    """
    post:
    Create a new trip. Requires authentication.
    Request body example:
    {
        "pickup_location": "Bandung",
        "dropoff_location": "Jakarta"
    }
    Response example:
    {
        "id": 1,
        "pickup_location": "Bandung",
        "dropoff_location": "Jakarta",
        "status": "Pending",
        "created_at": "2023-01-01T00:00:00Z",
        "updated_at": "2023-01-01T01:00:00Z"
    }
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TripStatusView(generics.ListAPIView):
    """
    get:
    Get the current user's trip status. Requires authentication.
    """
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)

class AvailableTripsView(generics.ListAPIView):
    """
    get:
    Get all available trips for drivers. Requires authentication.
    """
    queryset = Trip.objects.filter(status='Pending')
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

class AcceptTripView(APIView):
    """
    post:
    Accept a trip. Requires authentication.
    URL: /api/driver/trips/{trip_id}/accept/
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, trip_id, *args, **kwargs):
        trip = Trip.objects.get(id=trip_id)

        if trip.status != 'Pending':
            return Response({'message': 'Trip already accepted'}, status=status.HTTP_400_BAD_REQUEST)

        trip.status = 'Accepted'
        trip.save()

        order_trip = OrderTrip.objects.create(trip=trip, driver=request.user)
        return Response({'message': 'Trip accepted successfully'})
