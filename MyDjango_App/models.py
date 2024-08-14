from django.contrib.auth.models import User
from django.db import models
#
# # Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile', blank=True)

    def __str__(self) -> str:
        return self.user.username