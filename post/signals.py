from django.db.models.signals import pre_save
from django.dispatch import receiver

from post.models import Post


# @receiver(pre_save, sender=Post)
# def update_post(sender, instance, **kwargs):
#