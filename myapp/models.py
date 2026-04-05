def delete(self, using=None, keep_parents=False):
        pk = self.pk
        super().delete(using=using, keep_parents=keep_parents)
        if pk:
            self.pk = None