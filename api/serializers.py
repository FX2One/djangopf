from rest_framework import serializers
from .models import Article

#Serializer to serialize our Article class
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'author'
        ]
        






