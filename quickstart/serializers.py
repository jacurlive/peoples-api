from rest_framework import serializers
from .models import Peoples, Category


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peoples
        fields = ("id", "name", "last_name", "nickname", "content", "birth_date", "cat")


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ("name",)

    # name = serializers.CharField(max_length=150)

    # def create(self, validated_data):
    #     return Category.objects.create(**validated_data)
