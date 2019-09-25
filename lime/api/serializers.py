from rest_framework import serializers
from ..models import Bookmark, Category
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class BookmarkSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    
    class Meta:
        model = Bookmark
        fields = ['id', 'author','title', 'url', 'ico',
                  'description', 'created','updated','is_public','is_valid','category','tags']


class CategorySerializer(serializers.ModelSerializer):
    coco = BookmarkSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description','coco']

    def create(self, validated_data):
        cocos_data = validated_data.pop('coco')
        category = Category.objects.create(**validated_data)
        for coco_data in cocos_data:
            Bookmark.objects.create(category=category, **coco_data)
        return category


