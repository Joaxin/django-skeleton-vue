from rest_framework import serializers
from ..models import Message, Category
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class MessageSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    
    class Meta:
        model = Message
        fields = ['id', 'author','created','updated','content','category','tags']


class CategorySerializer(serializers.ModelSerializer):
    mensaje = MessageSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description','mensaje']

    def create(self, validated_data):
        cocos_data = validated_data.pop('mensaje')
        category = Category.objects.create(**validated_data)
        for coco_data in cocos_data:
            Message.objects.create(category=category, **coco_data)
        return category


