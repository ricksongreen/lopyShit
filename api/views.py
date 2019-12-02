from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.models import Toilet, Usage, Reviller, Revill
from api.serializers import UserSerializer, GroupSerializer, ToiletSerializer, UsageSerializer, RevillerSerializer, RevillSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ToiletViewSet(viewsets.ModelViewSet):
    queryset = Toilet.objects.all()
    serializer_class = ToiletSerializer

class UsageViewSet(viewsets.ModelViewSet):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer

class RevillerViewSet(viewsets.ModelViewSet):
    queryset = Reviller.objects.all()
    serializer_class = RevillerSerializer

class RevillViewSet(viewsets.ModelViewSet):
    queryset = Revill.objects.all()
    serializer_class = RevillSerializer
