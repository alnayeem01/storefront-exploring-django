from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class LikedItem(models.Model):
    # User : we imported this class from djanog auth.models module.
    # One User : Many likedItem
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # now we will define generic type of the object 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_id = models.PositiveIntegerField()
    # Qury field for whoel object
    content_object= GenericForeignKey()