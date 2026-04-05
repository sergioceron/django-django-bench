@receiver(post_delete, sender=MyModel)
def clear_pk_after_delete(sender, instance, **kwargs):
    # Set instance pk to None after deletion
    instance.pk = None
        super().delete(using=using, keep_parents=keep_parents)
        self.pk = None
        pk = self.pk
        super().delete(using=using, keep_parents=keep_parents)
        if pk:
            self.pk = None