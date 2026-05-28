from rest_framework import serializers
from blogs.models import BlogsModel, CommentsModel


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentsModel
        fields='__all__'

class BlogsSerializer(serializers.ModelSerializer):
    comments=CommentsSerializer(many=True,read_only=True)
    class Meta:
        model=BlogsModel
        fields='__all__'