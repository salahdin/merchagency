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

    uploadDate = models.DateTimeField(
        verbose_name="date and time of upload",
        null=False,
        auto_created=True,
        default=timezone.now
    )

    description = models.TextField(
        verbose_name="service/product description",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.Service_name
