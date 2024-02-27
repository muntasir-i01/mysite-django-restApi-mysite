from rest_framework import serializers
from .models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id','title', 'author', 'email', 'date']
        fields = '__all__'




# Function based api view using serializer

# what does serializer do and which api function based/ class based / generics api will I use in which time. 