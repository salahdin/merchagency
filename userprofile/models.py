from django.db import models
from core.models import Service
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following")
    following_user_id = models.ForeignKey(Service, related_name="followers")
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ("user_id", "following_user_id")
        ordering = ["-created"]

    def __str__(self):
        f"{self.user_id} follows {self.following_user_id}"
