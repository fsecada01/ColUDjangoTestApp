from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from main import models
from django.contrib.auth.models import User
from main.serializers import *


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


# Viewsets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwargs = 'username'

    def get_queryset(self):
        return self.queryset.filter(
            username=self.request.user.username)

    @action(detail=True)
    def group_names(self, request, pk=None):
        '''
        Returns a list of all the group names to which the selected user
        belongs
        '''

        user = self.get_object()
        groups = user.groups.all()
        return Response([group.name for group in groups])


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = AuthorSeralizer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class SubscriberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Subscriber.objects.select_related('user').all()
    serializer_class = SubscriberSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = models.Subscription.objects.select_related(
        'subscriber').select_related('book').all()
    serializer_class = SubscriptionSerializer


class ExpiredViewSet(SubscriptionViewSet):
    queryset = models.Subscription.expired_subs.all()
