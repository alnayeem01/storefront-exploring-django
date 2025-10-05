from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    #what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # To reduce dependecy between appps we will ignore this type of relationship
    # This will make the Tag appp dependent on Store
    # product = models.ForeignKey(product, on_delete=models.CASCADE)
    # To resolve this we will use Generic type
    # From django installed apps import this -     
    # 'django.contrib.contenttypes', it willl let us declare generic type fileds
    # Type : item type 
    # Id : item id
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # usign this field we can actually query the object added in the tag
    content_object = GenericForeignKey()

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
