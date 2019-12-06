from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Toilet, Usage, Tag, Refiller, Refill

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
        fields = ['id', 'name', 'place', 'toiletPaper']

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


class TagSerializer(serializers.HyperlinkedModelSerializer):
    model = Tag
    fields = ['uid']

class RefillerSerializer(serializers.HyperlinkedModelSerializer):
    tagUid = serializers.CharField( 
        source="tag.uid", read_only="True"
    )

    class Meta:
        model = Refiller
        fields = ['id', 'name', 'tagUid']

class RefillSerializer(serializers.HyperlinkedModelSerializer):
    toiletName = serializers.CharField(
        source="toilet.name", read_only="True"
    )
    toiletPlace = serializers.CharField(
        source="toilet.place", read_only="True"
    )
    toiletPaper = serializers.CharField(
        source="toilet.toiletPaper", read_only="True"
    )

    refillerName = serializers.CharField(
        source="refiller.name", read_only="True"
    )
    
    class Meta:
        model = Refill
        fields = ['id','refillDateTime', 'refiller', 'refillerName', 'toilet', 'toiletName', 'toiletPlace', 'toiletPaper']
