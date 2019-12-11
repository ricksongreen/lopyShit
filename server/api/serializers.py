from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Toilet, Usage, Tag, Refiller, Refill


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = [
            "id",
            "place",
            "toiletPaper",
            "maxAmountOfToiletRolls",
            "toiletRollSize",
            "extraDistance",
        ]


class UsageSerializer(serializers.ModelSerializer):
    toiletPlace = serializers.CharField(source="toilet.place", read_only="True")
    toiletPaper = serializers.CharField(source="toilet.toiletPaper", read_only="True")

    class Meta:
        model = Usage
        fields = ["id", "usageDateTime", "toilet", "toiletPlace", "toiletPaper"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["uid"]


class RefillerSerializer(serializers.ModelSerializer):
    tagUid = serializers.CharField(source="tag.uid", read_only="True")

    class Meta:
        model = Refiller
        fields = ["id", "name", "tag", "tagUid"]


class RefillSerializer(serializers.ModelSerializer):
    toiletPlace = serializers.CharField(source="toilet.place", read_only="True")
    toiletPaper = serializers.CharField(source="toilet.toiletPaper", read_only="True")

    refillerName = serializers.CharField(source="refiller.name", read_only="True")

    class Meta:
        model = Refill
        fields = [
            "id",
            "refillDateTime",
            "refiller",
            "refillerName",
            "toilet",
            "toiletPlace",
            "toiletPaper",
        ]
