from api_basic.models import Article
from api_basic.serializers import ArticleSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



a = Article(title = 'Can Israel be stopped from using starvation as a weapon of war?', author = 'Al Jazeera Staff', email = 'america@aljazeera.net', date = '21 Feb, 2024')
a.save()

# create serializer & we are going to pass our article in here.
serializer = ArticleSerializers(a)

serializer.data # by this we have translated a model instance into python native data type (dictionary)

# now we need to finalize the serialization process we need render this data into json

content = JSONRenderer().render(serializer.data)  

# To see the content in serialized (json) format

content

# if we want to add query set than
serializer = ArticleSerializers(Article.objects.all(), many = True)