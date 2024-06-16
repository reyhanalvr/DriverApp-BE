from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView, CreateTripView, TripStatusView, AvailableTripsView, AcceptTripView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('trips/', CreateTripView.as_view(), name='create_trip'),
    path('trips/status/', TripStatusView.as_view(), name='trip_status'),
    path('driver/trips/', AvailableTripsView.as_view(), name='available_trips'),
    path('driver/trips/<int:trip_id>/accept/', AcceptTripView.as_view(), name='accept_trip'),
]
