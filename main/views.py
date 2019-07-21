from django.shortcuts import render
from rest_framework import viewsets
from main import models
from django.contrib.auth.models import User
from main.serializers import *


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


# Viewsets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = AuthorSeralizer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = models.Subscriber.objects.select_related('user').all()
    serializer_class = SubscriberSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = models.Subscription.objects.select_related(
        'subscriber').select_related('book').all()
    serializer_class = SubscriptionSerializer


class ExpiredViewSet(SubscriptionViewSet):
    queryset = models.Subscription.expired_subs.all()
