from django.db import models
from core.models import Service
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="userprofile"
                             )
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatar/',verbose_name="user avatar", null=True,blank=True)


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(Service, related_name="following", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ("user_id", "following_user_id")
        ordering = ["-created"]

    def __str__(self):
        return str(f"{self.user_id} follows {self.following_user_id}")


class UserAddress(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="useraddress"
                             )
    link = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.link)