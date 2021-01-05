from rest_framework import serializers
from .models import Article

#Serializer to serialize our Article class
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validate_data.get('title', instance.title)
        instance.author = validate_data.get('title', instance.author)
        instance.email = validate_data.get('title', instance.email)
        instance.date = validate_data.get('title', instance.date)

