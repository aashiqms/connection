from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.utils.deconstruct import deconstructible


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    about_me = models.TextField(max_length=300, null=True)
    favourite_tv_shows = models.TextField(max_length=300, null=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    # age = models.PositiveIntegerField(default=18)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        """
        where user should be redirected after click post button
        :return:

        """
        return reverse('accounts:detail', kwargs={"pk": self.pk})  # 'slug': self.slug
