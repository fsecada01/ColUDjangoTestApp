from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
router.register('subscribers', views.SubscriberViewSet)
router.register('subscriptions', views.SubscriptionViewSet)
router.register('expired_subscrpts', views.ExpiredViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
