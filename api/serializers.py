from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Toilet, Usage, Reviller, Revill

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ToiletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toilet
        fields = ['id', 'place', 'toiletPaper']

class UsageSerializer(serializers.HyperlinkedModelSerializer):
    toiletName = serializers.CharField(
        source="toilet.name", read_only="True"
    )
    toiletPlace = serializers.CharField(
        source="toilet.place", read_only="True"
    )
    toiletPaper = serializers.CharField(
        source="toilet.toiletPaper", read_only="True"
    )

    class Meta:
        model = Usage
        fields = ['id', 'usageDateTime', 'toilet', 'toiletName', 'toiletPlace', 'toiletPaper']

class RevillerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviller
        fields = ['id', 'name', 'tag']

class RevillSerializer(serializers.HyperlinkedModelSerializer):
    toiletName = serializers.CharField(
        source="toilet.name", read_only="True"
    )
    toiletPlace = serializers.CharField(
        source="toilet.place", read_only="True"
    )
    toiletPaper = serializers.CharField(
        source="toilet.toiletPaper", read_only="True"
    )

    revillerName = serializers.CharField(
        source="reviller.name", read_only="True"
    )
    revillerTag = serializers.CharField(
        source="reviller.tag", read_only="True"
    )

    class Meta:
        model = Revill
        fields = ['id','revillDateTime', 'reviller', 'revillerName', 'revillerTag', 'toilet', 'toiletName', 'toiletPlace', 'toiletPaper']
