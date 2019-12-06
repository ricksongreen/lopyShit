from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.models import Toilet, Usage, Refiller, Refill, Tag
from api.serializers import UserSerializer, GroupSerializer, TagSerializer, ToiletSerializer, UsageSerializer, RefillerSerializer, RefillSerializer


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

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class RefillerViewSet(viewsets.ModelViewSet):
    queryset = Refiller.objects.all()
    serializer_class = RefillerSerializer

class RefillViewSet(viewsets.ModelViewSet):
    queryset = Refill.objects.all()
    serializer_class = RefillSerializer
