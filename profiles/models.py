from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Returns a string representation of the object.

    Returns:
        A string representation of the object.

    Examples:
        >>> str_representation = str(self)
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
