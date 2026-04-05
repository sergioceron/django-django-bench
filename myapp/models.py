def delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)
        object_deleted = not MyModel.objects.filter(pk=self.pk).exists()
        if object_deleted:
            self.pk = None
        super().delete(using=using, keep_parents=keep_parents)
        self.pk = None
        pk = self.pk
        super().delete(using=using, keep_parents=keep_parents)
        if pk:
            self.pk = None