from django.contrib.auth.models import User
from main import models
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'date_joined')


class AuthorSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Subscriber
        fields = '__all__'


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Subscription
        fields = '__all__'
