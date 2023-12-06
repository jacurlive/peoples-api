from rest_framework import serializers
from .models import Peoples, Category


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peoples
        fields = ("id", "name", "last_name", "nickname", "content", "birth_date", "cat")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
