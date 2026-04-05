def delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)
        self.pk = None
        pk = self.pk
        super().delete(using=using, keep_parents=keep_parents)
        if pk:
            self.pk = None