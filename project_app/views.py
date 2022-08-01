from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,DestroyAPIView

from project_app.models import Trip
from .serializers import CreateTripSerializer, TripListSerializer, UserCreateSerializer, UserLoginSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

class CreateTripView(CreateAPIView):
    serializer_class = CreateTripSerializer

class TripListView(ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripListSerializer
    
class TripUpdateView(UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = CreateTripSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    
class TripDeleteView(DestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    
class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    
class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)