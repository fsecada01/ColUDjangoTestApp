from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import make_aware
from django.utils.translation import ugettext as _
from datetime import datetime, timedelta


def time_diff(days):
    return make_aware(datetime.now() - timedelta(days))


class OutstandingSubscriptionManager(models.Manager):
    # a qs manager that presumes a subscription date of 30 days or less
    def get_queryset(self):
        return super().get_queryset().filter(
            borrowed_date__lte=time_diff(30)).filter(returned=False)


class ExpiredSubscriptionManager(models.Manager):
    # a qs manager that presumes a subscription date of 30 days or less
    def get_queryset(self):
        return super().get_queryset().filter(
            borrowed_date__lte=time_diff(30)).filter(returned=True)


class BaseUserModel(models.Model):
    name = models.CharField(_('Full Name'), max_length=25)
    # would probably be best to import a 3rd party module to split this into
    # discrete address fields
    address = models.CharField(_('Address'), max_length=512)

    class Meta:
        abstract = True


class Author(BaseUserModel):
    class Meta:
        verbose_name = 'Author'


class Book(models.Model):
    title = models.CharField(_('Book Title'), max_length=100)
    description = models.TextField(_('Book Description'))
    count = models.PositiveIntegerField(_('Book Count'))
    subscription_cost = models.PositiveIntegerField(_('Subscription Cost'))
    topic = models.CharField(_('Book Topic'), max_length=20)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Subscriber(BaseUserModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # PositiveIntegerField does not allow for length limiting, so CharField in
    # the model instance and Regex Validation in the Form Instance will
    # achieve the same result.
    phone = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Subscriber'


class Subscription(models.Model):
    subscriber = models.OneToOneField(Subscriber, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    # choose auto_add_now for creation presuming that borrowing dates will be
    # entered on a per-instance basis.
    borrowed_date = models.DateField(auto_now_add=True)
    amount_pad = models.PositiveIntegerField(_('Amount Paid'))
    returned = models.BooleanField(_("Book Returned?"))

    objects = models.Manager()

    outstand_subs = OutstandingSubscriptionManager()

    expired_subs = ExpiredSubscriptionManager()
