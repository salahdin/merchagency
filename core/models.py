from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Service(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="seller")
    Service_name = models.CharField(
        verbose_name="product/service name",
        null=False,
        max_length=50,
    )

    createDate = models.DateTimeField(
        verbose_name="date and time created",
        null=False,
        auto_created=True,
        default=timezone.now
    )

    description = models.TextField(
        verbose_name="service/product description",
        null=True,
        blank=True
    )

    avi = models.ImageField(null=True, blank=True, upload_to='avatar/')


    def __str__(self):
        return self.Service_name


class Post(models.Model):
    postby = models.ForeignKey(Service,
                               on_delete=models.CASCADE,
                               related_name="servicepost"
                               )
    postText = models.TextField(null=False, blank=False,verbose_name="post text")
    postImage = models.ImageField(upload_to="element/", null=True)
    postCreated = models.DateTimeField(auto_now=True)
    price = models.CharField(max_length=15, null=True, verbose_name="price of item",blank=True)

    def __str__(self):
        return self.postText[:25]

