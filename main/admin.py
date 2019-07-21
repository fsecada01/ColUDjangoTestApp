from django.contrib import admin as django_admin
from main.models import *


django_admin.site.register(Author)
django_admin.site.register(Book)
django_admin.site.register(Subscriber)
django_admin.site.register(Subscription)
