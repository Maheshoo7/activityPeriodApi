from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, ActivityPeriodSerializer
from .models import User, ActivityPeriod


class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

