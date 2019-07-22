from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rest_framework.routers import (Route,
                                    DynamicRoute,
                                    SimpleRouter,
                                    DefaultRouter)
from main import views as main_views


class CustomReadOnlyRouter(DefaultRouter):
    '''
    A router for read-only APIS; does not use trailing slashes
    '''

    routes = [
        Route(
            url='{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),

        Route(
            url='{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),

        DynamicRoute(
            url='{prefix}/{lookup}/{url_path}/$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
    ]


cust_router = CustomReadOnlyRouter()
cust_router.register('authors', main_views.AuthorViewSet)
cust_router.register('books', main_views.BookViewSet)

router = routers.DefaultRouter()
router.register('users', main_views.UserViewSet)
router.register('subscriptions', main_views.SubscriptionViewSet)
router.register('subscribers', main_views.SubscriberViewSet)
router.register('expired_subscripts', main_views.ExpiredViewSet)

urlpatterns = [
    path('api/', include(cust_router.urls)),
    path('subscriptions/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
]
