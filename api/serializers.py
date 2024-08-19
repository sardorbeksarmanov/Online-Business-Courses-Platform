from rest_framework import serializers
from .models import Comment, Clients, Serves, Advise, FAQs, Features


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serves
        fields = ['id', 'title', 'image', 'description', 'slug', 'price','views']
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'image', 'username', 'defination')


class CommentsSerializer(serializers.ModelSerializer):
    serves = ServiceSerializer()
    clients = ClientSerializer()

    class Meta:
        model = Comment
        fields = ('comment', 'clients', 'serves')


class AdvisersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advise
        fields = ['slug', 'first_name', 'last_name', 'email', 'phone', 'image', 'level', 'telegram_link', 'linkedin_link']


class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQs
        fields = ('questions', 'answers')


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('title', 'description')
