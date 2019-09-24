from rest_framework import serializers
from ..models import Bookmark, Category
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BookmarkSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    
    class Meta:
        model = Bookmark
        fields = ['id', 'author', 'category','title', 'url', 'ico',
                  'description', 'created','updated','is_public','is_valid','tags']


