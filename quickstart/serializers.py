from rest_framework import serializers
from .models import Peoples, Category


class PeopleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=155)
    last_name = serializers.CharField(max_length=155)
    nickname = serializers.CharField(max_length=155, allow_null=True, allow_blank=True)
    content = serializers.CharField()
    birth_date = serializers.DateField()
    is_published = serializers.BooleanField(default=False)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Peoples.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.content = validated_data.get("content", instance.content)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()

        return instance


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
