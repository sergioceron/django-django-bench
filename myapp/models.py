def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.pk = None
        super().delete(using=using, keep_parents=keep_parents)
        self.pk = None
        pk = self.pk
        super().delete(using=using, keep_parents=keep_parents)
        if pk:
            self.pk = None