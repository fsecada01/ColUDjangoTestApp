from django.contrib.auth.models import User
from main import models
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User


class AuthorSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Author


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Book


class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Subscriber


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Subscription
