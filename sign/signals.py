from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
from django.utils import timezone

@receiver(post_save, sender=Book)
def update_author_last_updated(sender, instance, **kwargs):



    # Update the Author's last_updated field when a Book is created or updated
     instance.author.last_updated = timezone.now()
     instance.author.save()



   