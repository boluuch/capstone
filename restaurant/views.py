from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import UserSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = UserSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = UserSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.object.all()
    serializer_class = UserSerializer
    Permission classes = [Perminssions.IsAuthenticated]
 """   