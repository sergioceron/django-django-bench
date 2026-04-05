def delete(self, using=None, keep_parents=False):
        super(MyModel, self).delete(using=using, keep_parents=keep_parents)
        if not self._state.adding and not MyModel.objects.filter(pk=self.pk).exists():
            self.pk = None
        super().delete(using=using, keep_parents=keep_parents)
        self.pk = None
        pk = self.pk
        super().delete(using=using, keep_parents=keep_parents)
        if pk:
            self.pk = None